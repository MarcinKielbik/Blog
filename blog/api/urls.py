from django.urls import path 
from . import views

urlpatterns = [
    path('blog-post', views.BlogPostList.as_view(), name='blogpsot-view-create')
]