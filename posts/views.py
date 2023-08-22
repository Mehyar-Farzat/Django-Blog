from django.shortcuts import render
from .models import post

# Create your views here.

def post_list(request):
    data = post.objects.all()
    return render(request,'all_posts.html', {'posts' : data})



def post_detail(request,post_id):
    data = post.objects.get(id=post_id)
    return render(request,'post_detail.html', {'post':data})
