from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gallery', views.gallery, name='gallery'),
    path('gallerys/<int:car_id>/', views.gallery_details, name='gallery_details'),
    path('services', views.services, name='services'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
   path('mail_send/', views.mail_send, name='mail_send'),
   path('mail_send_contact/', views.mail_send_contact, name='mail_send_contact'),
   path('mail_send_home/', views.mail_send_home, name='mail_send_home'),
]