from django.shortcuts import render, get_object_or_404
from .models import *
import markdown
from comments.forms import CommentForm
from comments.models import Comment


# Create your views here.

def index(request):
    p = Post.objects.all().order_by('-create_time')
    return render(request, 'blog/index.html', {
        'post_list': p
    })


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    form = CommentForm()
    comments = Comment.objects.filter(post=post)
    return render(request, 'blog/detail.html', {'post': post, 'comments': comments, 'form': form})


def archieves(request, year, month):
    print('%s,%s' % (year, month))
    p = Post.objects.filter(create_time__year=year, create_time__month=month).order_by('-create_time')
    print(len(p))
    return render(request, 'blog/index.html', {
        'post_list': p
    })


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    p = Post.objects.filter(category=cate)
    return render(request, 'blog/index.html', {
        'post_list': p
    })


def tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    p = Post.objects.filter(tags=tag)
    return render(request, 'blog/index.html', {
        'post_list': p
    })
