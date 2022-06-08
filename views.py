
from django.shortcuts import render
from .models import *
from .forms import CommentForm

def blog2_index(request):
    posts = post.objects.all().order_by('-created_on')

    context = {
        'posts': posts,

    }
    return render(request, 'blog2_index.html', context)


def blog2_detail(request, pk):
    posts = post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment=Comment(author=form.cleaned_data['author'],
                            body=form.cleaned_data['body'],
                            post=posts)
            comment.save()

    comments = Comment.objects.filter(post=posts)
    context = {
        'comments': comments,
        'form':form,
        'posts': posts,

    }
    return render(request, 'blog2_detail.html',context)

def blog2_category(request,category):
    posts=post.objects.filter(categories__name__contains=category).order_by('-created_on' )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)
