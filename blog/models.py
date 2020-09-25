from django.db import models
from django.utils import timezone

# Create your models here.
Post_Types = (

    ('Draft','Draft'),
    ('Published','Published'),

)
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=500, null=True, blank=True)
    Is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    author_mail = models.EmailField()
    image = models.ImageField(upload_to='post/')
    type = models.CharField(max_length=10, choices=Post_Types, default='Draft')


    def __str__(self):
        return self.title