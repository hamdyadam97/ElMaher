from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import translation
from post.forms import CommentForm
from post.models import Post, Comment
from section.models import Service
from user.forms import RegisterForm
from django.db.models.functions import TruncMonth
from django.db.models import Count


def post_list(request, service_slug=None):       # ← لقبول مسار اختياري
    posts = Post.objects.all().order_by('-created_at')
    form_signup = RegisterForm()
    form_signin = AuthenticationForm()
    current_lang = translation.get_language()
    service_obj = None
    if service_slug:
        service_obj = get_object_or_404(Service, slug=service_slug)
        posts = posts.filter(service=service_obj)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            post = get_object_or_404(Post, slug=request.POST.get('post_slug'))
            comment = form.save(commit=False)
            if request.user.is_authenticated:
                comment.user = request.user
            comment.post = post
            comment.save()
            return redirect(request.path)               # يعيد للفلتر نفسه
    else:
        form = CommentForm()

    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    archives = (
        Post.objects
            .annotate(month=TruncMonth('created_at'))
            .values('month')
            .annotate(post_count=Count('id'))
            .order_by('-month')
    )
    context = {
        'page_obj': page_obj,
        'form': form,
        'is_frontend_user': request.session.get('from_frontend', False),
        'services': Service.objects.all(),              # ← جميع الخدمات للودجت
        'current_service': service_obj,
        'lang': current_lang,
        'form_signup': form_signup,
        'form_signin': form_signin,
        'archives': archives,

    }
    return render(request, 'post/post_list.html', context)


def post_detail(request, slug):
    post = Post.objects.filter(slug=slug).first()
    form = CommentForm(request.POST or None)
    print(request.POST)

    if request.method == 'POST' and form.is_valid():
        comment = form.save(commit=False)
        comment.post = post

        # ربط المستخدم لو مسجل دخول
        if request.user.is_authenticated:
            comment.user = request.user

        # ربط التعليق بالأب إن وجد
        parent_id = request.POST.get("parent")
        if parent_id:
            try:
                comment.parent = Comment.objects.get(id=parent_id)
            except Comment.DoesNotExist:
                pass

        comment.save()
        return redirect('post:post_detail', slug=slug)
    archives = (
        Post.objects
            .annotate(month=TruncMonth('created_at'))
            .values('month')
            .annotate(post_count=Count('id'))
            .order_by('-month')
    )
    comments = post.comments.filter(parent__isnull=True).order_by('-created_at')
    return render(request, 'post/post_detail.html', {
        'post': post,
        'form': form,
        'services': Service.objects.all(),
        'comments': comments,
        'archives': archives,
    })


#
#
#
# def review_crud_page(request):
#     reviews = Review.objects.all().order_by('-created_at')
#     edit_review = None
#     form = ReviewForm()
#
#     # تعديل تقييم
#     if request.user.is_authenticated and 'edit_id' in request.GET:
#         edit_review = get_object_or_404(Review, pk=request.GET.get('edit_id'))
#         if edit_review.user != request.user and not request.user.is_superuser:
#             return redirect('furniture:review_crud_page')
#         form = ReviewForm(instance=edit_review)
#
#     # إضافة أو تعديل
#     if request.method == 'POST':
#         if 'edit_id' in request.POST:
#             if not request.user.is_authenticated:
#                 return redirect('furniture:review_crud_page')  # مش مسموح تعديل بدون دخول
#             edit_review = get_object_or_404(Review, pk=request.POST.get('edit_id'))
#             if edit_review.user != request.user and not request.user.is_superuser:
#                 return redirect('furniture:review_crud_page')
#             form = ReviewForm(request.POST, request.FILES, instance=edit_review)
#         else:
#             form = ReviewForm(request.POST, request.FILES)
#             print(form,'ssssssssssss')
#             print(form.is_valid(),'ssssssssssss')
#         if form.is_valid():
#             review = form.save(commit=False)
#             if request.user.is_authenticated:
#                 review.user = request.user
#             review.save()
#             return redirect('furniture:review_crud_page')
#
#     # حذف تقييم
#     if request.user.is_authenticated and 'delete_id' in request.GET:
#         review = get_object_or_404(Review, pk=request.GET.get('delete_id'))
#         if review.user == request.user or request.user.is_superuser:
#             review.delete()
#             return redirect('furniture:review_crud_page')
#
#     return render(request, 'furniture/review.html', {
#         'reviews': reviews,
#         'form': form,
#         'edit_review': edit_review,
#     })
#

# views.py

def post_archive(request, year, month):
    posts = Post.objects.filter(
        created_at__year=year,
        created_at__month=month
    ).order_by('-created_at')

    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # نفس الأرشيف للتنقل الجانبي
    archives = (
        Post.objects
        .annotate(month=TruncMonth('created_at'))
        .values('month')
        .annotate(post_count=Count('id'))
        .order_by('-month')
    )

    context = {
        'page_obj': page_obj,
        'archives': archives,
        'form': CommentForm(),
        'form_signup': RegisterForm(),
        'form_signin': AuthenticationForm(),
        'lang': translation.get_language(),
        'services': Service.objects.all(),
        'is_frontend_user': request.session.get('from_frontend', False),
    }

    return render(request, 'post/post_list.html', context)
