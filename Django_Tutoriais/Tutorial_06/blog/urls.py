from django.urls import path
<<<<<<< HEAD
from .views import (
    BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView
)
=======
from .views import BlogListView, BlogDetailView

>>>>>>> 0f34069531d58b2ce86903428c8cef0c7024d676
urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(),
    name='post_detail'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/',
        BlogUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/',
        BlogDeleteView.as_view(), name='post_delete'),
]