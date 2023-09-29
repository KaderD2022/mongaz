from django.http import request
from django.shortcuts import render, get_object_or_404


from myblog.models import Post, Comment
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.
from myblog.forms import CommentForm

def index(request):
    posts = Post.objects.all()
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
        'page': page,
    }
    return render(request, 'blog/index.html', context)


def detail(request, slug= str):
    post = get_object_or_404(Post, slug=slug)
    comments = Comment.objects.all()
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'blog/detail.html', {'post': post,
                                                'comment_form': comment_form,
                                                'comments': comments,
                                                'new_comment': new_comment,
                                               })


"""     comment = Comment.objects.all()
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(Commit=False)
            new_comment.post = post
            new_comment.save()
        else:
            new_comment = comment_form()

 """