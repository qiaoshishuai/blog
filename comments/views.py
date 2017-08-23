from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from .forms import CommentForm
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
# 客户端提交的post如果不加这段，会出现403error
@csrf_exempt
def post_comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)  # 参数带进去

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post

            comment.save()

            return redirect(post)
        else:
            comments = post.comment_set.all()
            context = {
                'post': post,
                'form': form,
                'comments': comments
            }
            return render(request, 'blog/detail.html', context)

    else:
        return redirect(post)
