from django.http import JsonResponse
from django.shortcuts import render
from django.core.paginator import Paginator
# Create your views here.


def landing_page(request):
    context = {
        'message': 'This is dynamic data from Django!',
        'items': ['Apple', 'Banana', 'Cherry'],
        'login_form': AuthenticationForm(),
        'is_frontend_user' : request.session.get('from_frontend', False)
    }
    return render(request, 'furniture/index.html', context)



from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Post, Service
from .forms import PostForm, CommentForm, RegisterForm

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

def frontend_signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            request.session['from_frontend'] = True
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'furniture/signup.html', {'form': form})


from django.contrib.auth import login as auth_login, authenticate, logout, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm


def frontend_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            request.session['from_frontend'] = True
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'furniture/login.html', {'form': form})




def frontend_logout(request):
    logout(request)
    request.session.flush()
    return redirect('/')


def post_list(request, service_slug=None):       # ← لقبول مسار اختياري
    posts = Post.objects.all().order_by('-created_at')

    # فلتر بالـ service إن وُجد
    service_obj = None
    if service_slug:
        service_obj = get_object_or_404(Service, slug=service_slug)
        posts = posts.filter(service=service_obj)

    # التعامل مع التعليقات (كما هو)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            post_id = request.POST.get('post_id')
            post = get_object_or_404(Post, pk=post_id)
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect(request.path)               # يعيد للفلتر نفسه
    else:
        form = CommentForm()

    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'form': form,
        'is_frontend_user': request.session.get('from_frontend', False),
        'services': Service.objects.all(),              # ← جميع الخدمات للودجت
        'current_service': service_obj,                 # ← المُختارة (إن وُجدت)
    }
    return render(request, 'furniture/post_list.html', context)