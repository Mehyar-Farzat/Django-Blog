from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from .models import post, comment


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ('title','publish_date', 'author')

admin.site.register(post,PostAdmin)
admin.site.register(comment)

