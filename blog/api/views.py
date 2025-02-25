from django.shortcuts import render
from rest_framework import generics

from blog.api.models import BlogPost
from blog.api.serializer import BlogPostSerializers

class BlogPostList(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializers