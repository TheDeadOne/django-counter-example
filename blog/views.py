from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView

from analytics.decorators import counted
from .models import Post


class PostList(ListView):
    model = Post


@method_decorator(counted, name='dispatch')
class PostDetail(DetailView):
    model = Post
