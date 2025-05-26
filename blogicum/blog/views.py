from django.shortcuts import get_object_or_404, render
from .models import Post, Category
from django.utils import timezone


def index(request):
    post_list = Post.objects.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True,
    ).order_by('-id')[:5]
    return render(request, 'blog/index.html', {'post_list': post_list})


def post_detail(request, post_id):
    post = get_object_or_404(
        Post.objects.select_related('category', 'author', 'location'),
        pk=post_id,
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True,
    )
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category.objects.filter(is_published=True), slug=category_slug
    )

    post_list = Post.objects.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__slug=category_slug,
    )
    context = {'post_list': post_list, 'category': category}

    return render(request, 'blog/category.html', context)
