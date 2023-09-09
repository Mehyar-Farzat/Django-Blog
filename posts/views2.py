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


class PostUpdate(generic.UpdateView):
    model = post
    fields = '__all__'
    success_url = '/blog/'
    template_name = 'posts/edit.html'

class PostDelete(generic.DeleteView):
    model = post
    success_url = '/blog/'
    

    
















