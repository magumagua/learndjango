from django.shortcuts import render_to_response, get_object_or_404
from .models import Blog, BlogType
from django.contrib.auth.models import User
# Create your views here.
def blog_list(request):
    context = {}
    context['blogs'] = Blog.objects.all()
    return render_to_response('blog_list.html', context)


def blog_detail(request, blog_pk):
    context = {}
    context['blog'] = get_object_or_404(Blog, pk=blog_pk)
    return render_to_response('blog_detail.html', context)

def blogs_with_type(request, blogs_with_type):
    context = {}
    blog_type = get_object_or_404(BlogType, pk=blogs_with_type)
    context['blogs'] = Blog.objects.filter(blog_type=blog_type)
    return render_to_response('blog_type.html', context)

def blogs_with_author(request, blogs_with_author):
    context = {}
    author = get_object_or_404(User, pk=blogs_with_author)
    context['blogs'] = Blog.objects.filter(author=author)
    return render_to_response('blogs_with_author.html', context)
