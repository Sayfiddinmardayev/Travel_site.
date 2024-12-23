from django.shortcuts import render, redirect
from .forms import PackageForm, SubscriptionForm
from .models import Package, Subscription
from apps.about.models import Post


def packageView(request):
    packages = Package.objects.all()
    form = PackageForm(request.POST or None, initial={'persons': 'ONE', 'kids': 1})
    subs = SubscriptionForm(request.POST or None, initial={'persons': 'ONE', 'kids': 1})
    post = Post.objects.all()

    if request.method == 'POST':
        print("Form errors: ", form.errors)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'packages.html', {
        'packages': packages,
        'form': form,
        "subs": subs,
        "posts": post
    })


def packageView2(request):
    subs = SubscriptionForm(request.POST or None, initial={'is_published': True})
    if request.method == 'POST':
        print("Form errors: ", subs.errors)
        if subs.is_valid():
            subs.save()
            return redirect('home')
    return render(request, 'packages.html', {
        'subs': subs,
    })