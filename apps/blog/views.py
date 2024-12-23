from django.shortcuts import render
from .models import Blog
from apps.package.forms import SubscriptionForm
from apps.about.models import Post


def blogView(request):
    subs = SubscriptionForm(request.POST or None)
    blog = Blog.objects.all().order_by('-id')
    post = Post.objects.all()
    return render(request, 'blog.html', {
        'blogs': blog,
        "subs": subs,
        "posts": post, 

    })