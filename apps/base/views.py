from django.shortcuts import render,redirect
from django.db.models import Count
from apps.about.models import About,Abot1,Guide, Post
from apps.service.models import Service, FeedbackClient
from apps.package.models import Package, BookingTour
from apps.package.forms import SubscriptionForm, PackageForm
from apps.blog.models import Blog
from apps.pages.models import TourCategory, OurCategory, Destination, Gallery


def indexView(request):
    about1 = Abot1.objects.all()
    about = About.objects.all()
    guide = Guide.objects.all().order_by('-id')[:4]
    service = Service.objects.all()
    feedbackclient = FeedbackClient.objects.all()
    package = Package.objects.all()
    subs = SubscriptionForm(request.POST or None)
    form = PackageForm(request.POST or None, initial={'persons': 'ONE', 'kids': 1})
    blog = Blog.objects.all().order_by('-id')
    destination = Destination.objects.prefetch_related('images').select_related('ctg')
    destination_ctg = OurCategory.objects.filter(status=False)
    gallery_ctg = OurCategory.objects.filter(status=True)
    gallery = Gallery.objects.prefetch_related('images').select_related('ctg')
    post = Post.objects.all()






    
# def packageView2(request):
#     subs = SubscriptionForm(request.POST or None, initial={'is_published': True})
#     if request.method == 'POST':
#         print("Form errors: ", subs.errors)
#         if subs.is_valid():
#             subs.save()
#             return redirect('home')
#     return render(request, 'packages.html', {
#              'subs': subs,
#     })

   
    

    return render(request, 'index.html',
                context={
                'abouts1':about1,
               'abouts': about,
                'guides': guide,
                'service1': service[1::],  # pass the services to the template:
                'service2': service[::1],  # pass the services to the template:
                'feedbackclients': feedbackclient,  
                'packages': package,
                "subs": subs,
                "form": form,
                'blogs': blog,
                "tour_category": TourCategory.objects.all(),
                'destination': destination.annotate(destination_num=Count('images')),
                'destination_ctg': destination_ctg,
                'gallery_ctg': gallery_ctg,
                'gallery': gallery,
                "posts": post,
                



                })

