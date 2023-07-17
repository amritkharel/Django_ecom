"""
URL configuration for lab1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from payment.views import khalti_payment_verify, message, pay, changepassword, changep
from item.views import show_items, show_items_admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('changep/', changep, name='pchange'),
    path('changepassword/', changepassword, name='passwordchange'),
    path('pay/',khalti_payment_verify, name='payment'),
    path('payment/', pay, name='pay'),
    path('message/', message, name='message'),
    path('cart/', include('cart.urls')),
    path('product/', include('product.urls')),
    path("showitems/", show_items, name='show_items'),
    path("showitemsadmin/", show_items_admin, name='show_items'),
]
