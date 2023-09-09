from django.views import generic
from .models import post


class PostList(generic.ListView):
    model = post


class PostDetail(generic.DetailView):
    model = post


class PostCreate(generic.CreateView):
    model = post
    fields = '__all__'
    success_url = '/blog/'






