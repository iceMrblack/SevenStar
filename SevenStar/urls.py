"""SevenStar URL Configuration

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

from seven_star import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('saveCompanyData/',views.save_company_data),
    # path('save_finance_data/',views.save_finance_data),
    # path('fill_stock_type/',views.fill_stock_type),
    path('save_static_data/',views.save_static_data),
]
