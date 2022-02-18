from django.urls import path
from .views import (
PostListView, 
PostDetailView,
PostCreateView,
PostNewView,
) 


urlpatterns = [
    path('', PostListView.as_view(), name="post_list"),
    path('posts/<int:pk>/', PostDetailView.as_view(), name="post_detail"),
    path('', PostNewView.as_view(), name="post_new"),
]