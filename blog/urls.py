from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    CommentCreateView,
)

urlpatterns = [
    path("", PostListView.as_view(), name="blog-home"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("about/", views.about, name="blog-about"),
    path("contributors/", views.contributors, name="blog-contributors"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("user/<str:username>/", UserPostListView.as_view(), name="user-posts"),
    path("post/<int:pk>/comment", CommentCreateView.as_view(), name="post-comment"),
]
# ListView will look for a template at <app>/<model>_<viewtype>.html
# PostCreateView shares its template with Update View
# it should be named as model_form.html