from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("api/posts", views.PostListAPIView.as_view(), name="api_post_list"),
    path(
        "api/posts/<int:pk>/", views.PostDetailAPIView.as_view(), name="api_post_detail"
    ),
]
