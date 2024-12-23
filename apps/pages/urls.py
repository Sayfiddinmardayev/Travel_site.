from django.urls import path
from django.conf.urls import handler404
from .views import (destination,
                    destination_tab,
                    explore_tour,
                    travel_booking,
                    our_gallery,
                    travel_guide,
                    testimonial, 
                    gallery_tab,
                    # custom_404
                    )
from apps.package.views import packageView2

urlpatterns = [
    path('destination/', destination, name='destination'),
    path('destination-tab/tab-<int:tab_id>/', destination_tab, name='destination_tab'),

    path('our_gallery/', our_gallery, name='gallery'),
    path('gallery-tab/tab-<int:tab_id>/', gallery_tab, name='gallery_tab'),

    path('explore_tour/', explore_tour, name='tour'),
    path('packageView2/', packageView2, name='package2'),
    path('travel_booking/', travel_booking, name='booking'),
    path('travel_guides/', travel_guide, name='guides'),
    path('testimonial/', testimonial, name='testimonial'),
    # path('404_page/', custom_404, name='404'),
]

handler404 = 'pages.views.custom_404'