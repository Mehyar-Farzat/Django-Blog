from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.

class post(models.Model):
    author = models.ForeignKey(User,related_name='post_author',on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=120)
    content = models.TextField(max_length=10000)
    publish_date = models.DateTimeField(default= timezone.now)
    tags = TaggableManager()
    image = models.ImageField(upload_to='posts', null=True)

    slug = models.SlugField(null=True, blank= True)
    
    
    def __str__(self) -> str:
        return self.title


    def save(self, *args, **kwargs ):
        
        self.slug = slugify(self.title)
        super(post, self).save(*args, **kwargs)


    


    





    

        
    
    
   
class comment(models.Model):
    author = models.ForeignKey(User,related_name='comment_author',on_delete=models.CASCADE)
    post = models.ForeignKey(post , related_name='comment_post', on_delete=models.CASCADE)
    comment = models.TextField(max_length=500)
    create_date = models.DateTimeField(default= timezone.now)


    def __str__(self) -> str:
        return self.comment