from django.urls import path
from .views import *
app_name='app1'
urlpatterns=[
    path('',home, name='home'),
    path('signup/',signup,name='signup'),
    path('login/',login,name='login'),
    path('orderonline/',orderonline, name='orderonline' ),
    path('profile/',profile,name='profile'),
    path('restaruant/',restaruant,name='restaruant'),
    path('dining',dining,name='dining'),
    path('events',events,name='events'),
    path('cart/',cart,name='cart'),
    path('reservation/',reservation,name='reservation')
]