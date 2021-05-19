from django.urls import path
from . import views

from .views import SearchUserPostListView

urlpatterns = [
    path("", views.search_page, name="search-page"),
    path(
        "<str:username>/",
        SearchUserPostListView.as_view(),
        name="search-user-posts",
    ),
]
