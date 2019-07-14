from django.urls import path

from .views import PostDetail, PostList

app_name = 'blog'
urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name='post'),
    path('', PostList.as_view(), name='index'),
]
