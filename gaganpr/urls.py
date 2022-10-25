from django.contrib import admin
from django.urls import path
from gaganpr import views 


urlpatterns = [
    path("", views.index, name='gaganpr'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.Contact, name='Contact'),
    path("myspace", views.myspace, name='myspace'),
    path("handlelogin", views.handlelogin, name='handlelogin'),
    path("data", views.Data, name='Data'),
    path("listings", views.listings, name='listings'),
    path("search", views.search, name='search'),
]
