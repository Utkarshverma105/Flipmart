"""Flipmart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from signup import views
from login import views1, lviews3
from userprofile import views2, views3, views4, views5
from Retailer import Rviews, Rviews2, Rviews3, Rviews4, Rviews5, Rviews6
from wholesale import Wviews, Wviews2, Wviews3, Wviews4, Wviews5, Wviews6
from Delivery_Agent import dviews1, dviews2, dviews3, dviews4
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views1.Login, name='login'),
    path('lotp/', lviews3.Lotp, name='lotp'),
    path('signup/', views.sign_up, name='signup'),
    path('profile/', views2.userprofile, name='profile'),
    path('shop_name/', views2.shop_name, name='shop_name'),
    path('dashboard/', views2.dashboard, name='dashboard'),
    path('update/', views3.update, name='update'),
    path('shopping_cart/', views4.shopping_cart, name='shopping_cart'),
    path('delivery/', views4.delivery, name='delivery'),
    path('feedback/', views5.feedback, name='feedback'),
    path('rlogin/', Rviews2.RLogin, name='rlogin'),
    path('rsignup/', Rviews.Rsign_up, name='rsignup'),
    path('rotp/', Rviews3.Rotp, name='rotp'),
    path('raccount/', Rviews4.Raccount, name='raccount'),
    path('rsetup/', Rviews5.Rsetup, name='rsetup'),
    path('rnear/', Rviews4.near, name='rnear'),
    path('ritem/', Rviews4.item, name='ritem'),
    path('rshop/', Rviews6.Shop_item, name='rshop'),
    path('rupdate/', Rviews6.update, name='rupdate'),
    path('wlogin/', Wviews2.WLogin, name='wlogin'),
    path('wsignup/', Wviews.Wsign_up, name='wsignup'),
    path('wotp/', Wviews3.Wotp, name='wotp'),
    path('waccount/', Wviews4.Waccount, name='waccount'),
    path('wsetup/', Wviews5.Wsetup, name='wsetup'),
    path('wupdate/', Wviews6.Wupdate, name='wupdate'),
    path('whistory/', Wviews5.history, name='whistory'),
    path('dlogin/', dviews1.dlogin, name='dlogin'),
    path('dotp/', dviews2.dotp, name='dotp'),
    path('dsignup/', dviews3.sign_up, name='dsignup'),
    path('ddashboard/', dviews4.order, name='ddashboard'),
]
