from django.urls import path 
from . import views

urlpatterns = [
    path('blog-post/', views.BlogPostListAdd.as_view(), name='blogpsot-view-create'),
    path('blog-post/<int:pk>/', views.BlogPostListUpdateDelete.as_view(), name='update')
]