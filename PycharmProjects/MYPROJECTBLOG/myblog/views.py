from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from myblog.models import Post, Comment, Category
from django.views import generic
from myblog.forms import CommentForm

def list_post(request, category=None):
    posts = Post.objects.all()
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
    except Emptypage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'posts':posts,
        'page': page,
        'category': category,
        'categories': categories,
    }
    return render(request, 'myblog/post/list-post.html', context)

""" class PostListView(generic.ListView):
    queryset = Post.objects.all()
    paginate_by = 2
    template_name = 'myblog/post/list-post.html'
    context_object_name = 'posts'

 """
def post_detail(request, slug: str):
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
    return render(request, 'myblog/post/list-detail.html', {'post': post,
                                                            'comments': comments,
                                                            'new_comment': new_comment,
                                                            'new_comment': new_comment,
                                                            'comment_form': comment_form,
                                                            })
