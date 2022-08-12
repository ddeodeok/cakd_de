from django.shortcuts import render
import sys
import os
# 부모 폴더의 절대경로를 참조 path에 추가하기
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from blog.models import Post, Category, Tag


def landing(request):
    return render(
        request,
        'single_pages/landing.html'
    )

def about_me(request):
    return render(
        request,
        'single_pages/about_me.html',
        {
            'categories': Category.objects.all(),
            'no_category_post_count': Post.objects.filter(category=None).count(),
        }
        
    )
# Create your views here.

