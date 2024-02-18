from django.urls import path
from .views import home, aboutpage

urlpatterns = [
    path('',home, name='home'),
    path('about/', aboutpage, name='about')
]