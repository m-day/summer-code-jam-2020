from django.urls import path, include
from .views import ImagePostListView, ImagePostDetailView

urlpatterns = [
    path("", ImagePostListView.as_view(), name="posts-home"),
    path("post/<int:pk>", ImagePostDetailView.as_view(), name="posts-detail"),
]