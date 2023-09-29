from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.transaction import commit
from django.http import request, HttpResponse
from django.shortcuts import render, get_object_or_404

from blog.forms import CommentForm, SearchForm
from blog.models import Post, Comment, Category, Reponse
from django.contrib.postgres.search import SearchVector

# from myblog.models import Category
# Create your views here.

def index(request, category=None):
    posts = Post.published.all()
    categories = Category.objects.all()
    if category:
        category = get_object_or_404(Category, slug=category)
        posts = posts.filter(category=category)

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
        'paginator': paginator,
        'category': category,
        'categories': categories,

    }
    return render(request, 'blog/index.html', context)


def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = Comment.objects.filter(post=post.id)

    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'blog/detail.html', context={
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'new_comment': new_comment,
    })


def post_search(request):

    query = None
    results = []
    search_form = SearchForm()
    if 'query' in request.GET:
        search_form = SearchForm(request.GET)
        if search_form.is_valid():
            query = search_form.cleaned_data['query']
            results = Post.published.filter(title__search='query')
    return render(request, 'blog/search.html', context={
        'query': query,
        'results': results,
        'search_form': search_form,

    })




