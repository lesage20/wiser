from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('blog', views.blog, name='blog'),
    path('admissions', views.admissions, name='admissions'),
    path('contact', views.contact, name='contact'),
    path('courses', views.courses, name='courses'),
    path('elements', views.elements, name='elements'),
    path('detail', views.detail, name='detail'),
    path('event', views.event, name='event'),
    path('main', views.main, name='main'),
    path('single', views.single, name='single'),
    # path('panel', views.panel, name='panel'),
]