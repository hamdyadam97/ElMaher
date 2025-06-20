from django.shortcuts import render
from django.core.paginator import Paginator
# Create your views here.


def landing_page(request):
    context = {
        'message': 'This is dynamic data from Django!',
        'items': ['Apple', 'Banana', 'Cherry']
    }
    return render(request, 'furniture/index.html', context)



from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Post
from .forms import PostForm, CommentForm

# صلاحية النشر
staff_admin = user_passes_test(lambda u: u.is_authenticated and u.role in ['staff', 'admin'])

@staff_admin
def post_create(request):
    form = PostForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('post_detail', pk=post.pk)
    return render(request, 'core/post_form.html', {'form': form})

# عرض البوست + إضافة تعليق (زائر أو مستخدم)
from .models import Comment

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        if request.user.is_authenticated:
            comment.user = request.user
        comment.save()
        return redirect('post_detail', pk=pk)
    return render(request, 'core/post_detail.html', {'post': post, 'form': form})

# إضافة تقييم شركة

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'core/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'core/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            post_id = request.POST.get('post_id')
            post = get_object_or_404(Post, pk=post_id)
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('post_list')
    else:
        form = CommentForm()

    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'furniture/post_list.html', {'page_obj': page_obj, 'form': form})