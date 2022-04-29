"""imports"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('addpost/', views.AddPost.as_view(), name='add_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name="post_detail"),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
]
