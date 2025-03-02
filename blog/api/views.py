from django.shortcuts import render
from rest_framework import generics

from .models import BlogPost
from .serializer import BlogPostSerializers

class BlogPostListAdd(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializers
    
    
class BlogPostListUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializers
    lookup_field = "pk"