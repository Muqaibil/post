from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display=['title','created_at','type','Is_active']
    list_filter=['Is_active']

admin.site.register(Post, PostAdmin)
