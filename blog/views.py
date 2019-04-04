
from django.shortcuts import render, get_object_or_404
from .models import *
import markdown
from comments.forms import CommentForm
from comments.models import Comment
from django.core.paginator import Paginator
from django.http import Http404,HttpResponse

# Create your views here.

def index(request):
    p = Post.objects.all().order_by('-create_time')
    return render(request, 'blog/index.html', {
        'post_list': p
    })

def about(request):
    return render(request,'blog/about.html')

def time(request):
    return render(request,'blog/time.html')

def kytime(request):
    return render(request,'blog/kytime.html')

def gktime(request):
    return render(request,'blog/gktime.html')

def kaoyan(request):
    return render(request,'blog/kaoyan.html')

def wxjs(request):
    return render(request,'MP_verify_KU3fTEITAMh5YMAZ.txt')

def error(request):
    return render(request,'blog/404.html')


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

def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    paginator = context.get('paginator')
    page = context.get('page_obj')
    is_paginated = context.get('is_paginated')
    pagination_data = self.pagination_data(paginator, page, is_paginated)
    context.update(pagination_data)
    return context

def pagination_data(self, paginator, page, is_paginated):
    if not is_paginated:
        return {}
    left = []
    right = []
    left_has_more = False
    right_has_more = False
    first = False
    last = False
    page_number = page.number
    total_pages = paginator.num_pages
    page_range = paginator.page_range
    if page_number == 1:
        right = page_range[page_number:page_number + 2]
        if right[-1] < total_pages - 1:
            right_has_more = True
        if right[-1] < total_pages:
            last = True
    elif page_number == total_pages:
        left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]
        if left[0] > 2:
            left_has_more = True
        if left[0] > 1:
            first = True
    else:
        left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]
        right = page_range[page_number:page_number + 2]
        if right[-1] < total_pages - 1:
            right_has_more = True
        if right[-1] < total_pages:
            last = True
        if left[0] > 2:
            left_has_more = True
        if left[0] > 1:
            first = True
    data = {
        'left': left,
        'right': right,
        'left_has_more': left_has_more,
        'right_has_more': right_has_more,
        'first': first,
        'last': last,
    }
    return data
