from typing import ContextManager
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator

# importing Posts data from database
from .models import Post, Comment
from .models import ImpLink

# dummy data
# posts = [
#     {
#         "author": "myname",
#         "title": "posttitle",
#         "content": "content posted",
#         "date_posted": "12th august",
#     }
# ]

# ListView will look for a template at <app>/<model>_<viewtype>.html
class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    # since we are passing context as posts in home view function
    #  but by default class calls it objectlist or we can change
    # the variable as below
    # negative sign means dates from newest to oldest
    #  and it sets the order of the posts
    context_object_name = "posts"
    paginate_by = 5
    ordering = ["-date_posted"]

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context["linkinfo"] = ImpLink.objects.all()
        list_exam = Post.objects.all().order_by("-id")
        paginator = Paginator(list_exam, self.paginate_by)

        page = self.request.GET.get("page")

        try:
            file_exams = paginator.page(page)
        except:
            file_exams = paginator.page(1)

        return context


class PostDetailView(DetailView):
    model = Post


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    # function tests so that other users cannot update posts
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# CreateView with a form to Create a Post it shares template with
#  update view
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]
    # overriding form vaild method to add author id
    # and name when a blog is created
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # this tells that form that we are trying
    # to submit before submitting set the author to current logged in user


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ["body"]
    template_name = "blog/comment.html"
    # overriding form vaild method to add author id
    # and name when a blog is created
    def form_valid(self, form):
        form.instance.name = self.request.user
        form.instance.post_id = self.kwargs["pk"]
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content"]
    # overriding form vaild method to add
    # author id and name when a blog is created
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # this tells that form that we are trying to submit
    #  before submitting set the author to current logged in user

    # function tests so that other users cannot update posts
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class UserPostListView(ListView):
    model = Post
    template_name = "blog/user_posts.html"
    context_object_name = "posts"
    # since we are passing context as posts in home view function
    #  but by default class calls it objectlist or we can change
    # the variable as below
    # negative sign means dates from newest to oldest
    #  and it sets the order of the posts
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Post.objects.filter(author=user).order_by("-date_posted")


# def home(request):
#     context = {"posts": Post.objects.all()}
#     return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})


def contributors(request):
    return render(request, "blog/contributors.html", {"title": "contributors"})
