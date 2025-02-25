from django.shortcuts import render
from rest_framework import generics

from .models import BlogPost
from .serializer import BlogPostSerializers

class BlogPostList(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializers