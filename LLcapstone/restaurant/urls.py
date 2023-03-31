from django.contrib import admin 
from django.urls import path 
from . import views
from .views import menuview,MenuItemsView,SingleMenuItemView
from rest_framework.authtoken.views import obtain_auth_token
  
urlpatterns = [ 
    path('', views.index, name='index'), 
    #path('booking/', bookingview.as_view()),
    #path('menu/', menuview.as_view()),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api-token-auth/',obtain_auth_token)
]