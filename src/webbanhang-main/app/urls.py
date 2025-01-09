from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('login/', views.log_in, name="login"),
    path('logout/', views.log_out, name="logout"),
    path('about/', views.about, name="about"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('search/', views.search, name="search"),
    path('category/', views.category, name="category"),
    path('statistics/', views.statistics_view, name="statistics"),
    path('featured_products/', views.featured_products, name='featured_products'),
]
