from django.shortcuts import render
from .models import Service, FeedbackClient
from apps.package.forms import SubscriptionForm
from apps.about.models import Post


def serviceView(request):
    service = Service.objects.all()
    feedbackclient = FeedbackClient.objects.all()
    subs = SubscriptionForm(request.POST or None, initial={'persons': 'ONE', 'kids': 1})
    post = Post.objects.all()


    return render(request, 'services.html', context={
        'service1': service[1::],  # pass the services to the template:
        'service2': service[::1],  # pass the services to the template:
        'feedbackclients': feedbackclient, # pass the latest 3 feedback clients to the template:
        "subs": subs,
        'posts': post,

    })
