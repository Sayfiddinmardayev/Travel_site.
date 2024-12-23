from django.shortcuts import render
from .models import About, Guide, Abot1, Post
from apps.package.forms import SubscriptionForm, PackageForm


def aboutView(request):
    about1 = Abot1.objects.all()
    about = About.objects.all()
    guide = Guide.objects.all().order_by('-id')[:4]
    subs = SubscriptionForm(request.POST or None)
    form = PackageForm(request.POST or None, initial={'persons': 'ONE', 'kids': 1})
    post = Post.objects.all()

    return render(request, 'about.html', 
                context={
                    'abouts1':about1,
                   'abouts': about,
                   'guides': guide,   
                    "subs": subs,
                   "form": form,
                   "posts": post,

                  })
