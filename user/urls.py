"""DesireCart URL Configuration

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

from django.urls import path

from . import views

urlpatterns = [
    path('mens/', views.mens),
    path('mens/men', views.mens),
    path('womens/', views.womens),
    path('contactus/', views.contact),
    path('kids/', views.kids),
    path('myoders/', views.myoders),
    path('myprofile/', views.myprofile),
    path('details/', views.detail),
    path('signup/', views.signUp),
    path('signin/', views.signin),
    path('signout/', views.signout),
    path('addtocart/', views.addtocart),
    path('orderdetails',views.orderdetails),
    path('cartdata/',views.cartdata),
    path('mycart/',views.mycart),
    path('checkuname/',views.uname),
    path('removefromcart/',views.removefromcart),
    path('payment/',views.payment),
    path('thanks/',views.thanks),
    path('track/',views.track),
    path('editpro/',views.editpro),
    path('saveedit/',views.saveedit),
    path('forgetpassword/',views.forgetpassword),
    path('data/',views.data),


]
