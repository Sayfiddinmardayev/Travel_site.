from django.shortcuts import render, redirect
from .models import ContactMe, Contact
from apps.package.forms import SubscriptionForm
from apps.about.models import Post




def contactView(request):
    subs = SubscriptionForm(request.POST or None)
    contact = ContactMe.objects.first()
    post = Post.objects.all()

    if request.method == 'POST':
        data = request.POST
        Contact.objects.create(
            full_name=data.get('name'),
            email=data.get('email'),
            subject=data.get('subject'),
            message=data.get('msg')
        )
        return redirect('contact')
    
    return render(request, 'contact.html', context={
        "contact": contact,
        "subs": subs,
        "posts": post,

    })