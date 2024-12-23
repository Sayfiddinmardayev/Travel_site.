from django.urls import path
from .views import contactView

from apps.package.views import packageView2

urlpatterns = [
    path('', contactView, name='contact'),   
    path('packageView2/', packageView2, name='package2'),

]