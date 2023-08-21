from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class post(models.Model):
    author = models.ForeignKey(User,related_name='post_author',on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=120)
    content = models.TextField(max_length=10000)
    publish_date = models.DateTimeField()
    
    def __str__(self) -> str:
        return self.title
    
    
    def __str__(self) -> str:
        return self.content

   
    