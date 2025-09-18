from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('',views.index),
    path('open_signin/', views.open_signin, name='open_signin'),
    path('open_signup/', views.open_signup, name='open_signup'),
    path('signup/', views.signup, name ='signup'),
    path('signin/', views.signin, name ='signin'),
    path('signin/open_add_restaurant/', views.open_add_restaurant,
          name ='open_add_restaurant'),
    path('signin/open_show_restaurant/', views.open_show_restaurant,
          name ='open_show_restaurant'),      
    path('add_restaurant/', views.add_restaurant,name ='add_restaurant'),
    path('add_restaurant/open_update_restaurant/<int:restaurant_id>', views.open_update_restaurant,name ='open_update_restaurant'),
    path('update_restaurant/<int:restaurant_id>',views.update_restaurant,name="update_restaurant"),
    path('delete_restaurant/<int:restaurant_id>',views.delete_restaurant,name="delete_restaurant") ,
    path('add_restaurant/open_add_item/<int:restaurant_id>/', views.open_add_item, name='open_add_item'),
    path('add_item/<int:restaurant_id>/', views.add_item, name='add_item'),
    path('view_items/<int:restaurant_id>/', views.view_items, name='view_items'),
]