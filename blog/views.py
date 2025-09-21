from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer


def post_list(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request, "blog/post_list.html", {"posts": posts})


class PostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.order_by("-created_at")
    serializer_class = PostSerializer


class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
