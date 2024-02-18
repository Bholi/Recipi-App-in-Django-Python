from django.urls import path
from .views import recipipage, delete_recipi,update_recipi,register_page,login_page,logout_page
urlpatterns = [
    path('recipi/',recipipage, name='recipi'),
    path('deleterecipi/<id>',delete_recipi, name='deleteRecipi'),
    path('updaterecipi/<id>', update_recipi, name= 'updateRecipi'),
    path('register/', register_page, name='register'),
    path('login/', login_page, name='login'),
    path('logout/',logout_page, name='logout' ),
]