from unicodedata import name
from django.urls import path
from poll.views import Index,ContactUs,AboutUs,Main,info

app_name="poll"

urlpatterns=[
path('',Index,name="index"),
path("contact/us/",ContactUs,name="contact"),
path('about/us/',AboutUs,name="about"),
path('main/',Main,name="main"),
path('info/',info,name="info")

]
