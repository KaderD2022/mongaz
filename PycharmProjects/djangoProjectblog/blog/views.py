from django.shortcuts import render, get_object_or_404

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from blog.forms import CommentForm
from blog.models import Post, Comment


# Create your views here.

def index(request): 
    posts = Post.objects.all()
    comments = Comment.objects.all()
    new_comments = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST) 
        if comment_form.is_valid():
            new_comments = CommentForm(commit=False)
            new_comments.posts = posts
            new_comments.save()
        else:
            new_comments = CommentForm
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'posts': posts,
        'paginator': paginator,
        'page': page,
    }
    return render(request, 'blog/index.html', context)


def detail(request, slug=None):
    post = get_object_or_404(Post, slug=slug)

    return render(request, 'blog/detail.html', {'post':post})