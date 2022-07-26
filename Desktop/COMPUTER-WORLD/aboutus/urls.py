from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.aboutus, name='aboutus'),
    path('newsletter_signup/', views.newsletter_signup, name='newsletter_signup'),
    path('newsletter_unsubscribe/', views.newsletter_unsubscribe,
         name='newsletter_unsubscribe'),
    path('sitemap/', views.sitemap, name='sitemap'),

]
