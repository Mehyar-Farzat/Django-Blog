from django.db import models

# Create your models here.

class post(models.Model):
    title = models.CharField("Title", max_length=120)
    content = models.TextField("content",max_length=10000)
    publish_date = models.DateTimeField()

   
    