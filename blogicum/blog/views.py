from django.shortcuts import get_object_or_404, render

from .models import Category, Post


DISPLAY_VIEW_NUM = 5


def index(request):
    post_list = Post.objects.published().filter(
        category__is_published=True,
    )[:DISPLAY_VIEW_NUM]
    return render(request, 'blog/index.html', {'post_list': post_list})


def post_detail(request, post_id):
    post = get_object_or_404(
        Post.objects.published().select_related(
            'category',
            'author',
            'location'
        ),
        pk=post_id,
        category__is_published=True,
    )
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category.objects.filter(is_published=True), slug=category_slug
    )

    post_list = Post.objects.published().filter(
        category__slug=category_slug,
    )
    context = {'post_list': post_list, 'category': category}

    return render(request, 'blog/category.html', context)
