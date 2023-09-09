from django.views import generic
from .models import post


class PostList(generic.ListView):
    model = post


class PostDetail(generic.DetailView):
    model = post



