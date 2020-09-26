from django.shortcuts import render
from blog.models import Post
# Create your views here.

def post_list(request):
    all_posts = Post.objects.all()
    return render(request, 'Post/post_list.html',{'posts':all_posts} )
    pass

def post_details (request):
    pass
