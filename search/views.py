from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, request, HttpResponseRedirect
from blog.models import Post
from django.urls import reverse
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
)
from django.http import Http404

# Create your views here.
def search_page(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        if searched:
            return HttpResponseRedirect(
                reverse("search-user-posts", kwargs={"username": searched})
            )
        else:
            return render(request, "search/search_page.html", {})

    else:
        return render(request, "search/search_page.html", {})


class SearchUserPostListView(ListView):
    model = Post
    template_name = "search/search_user_posts.html"
    context_object_name = "posts"
    # since we are passing context as posts in home view function
    #  but by default class calls it objectlist or we can change
    # the variable as below
    # negative sign means dates from newest to oldest
    #  and it sets the order of the posts
    paginate_by = 5

    def get_queryset(self):
        try:
            user = User.objects.get(username__istartswith=self.kwargs.get("username"))
            return Post.objects.filter(author=user).order_by("-date_posted")
        except:
            return User.objects.none()
