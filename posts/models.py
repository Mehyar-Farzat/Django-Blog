from django.db import models

# Create your models here.

class post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(max_length=10000)
    publish_date = models.DateTimeField()

   
    