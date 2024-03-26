"""
URL configuration for ajeevi_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from ajeevi_app.views import *
router = DefaultRouter()
router.register(r'user-admin', test_data)
router.register(r'master-table',master_table)
router.register(r'address-data',address_table)
router.register(r'entity-type',entity_table)
router.register(r'contact-data',contact_table)
router.register(r'branch-table',branch_table)
router.register(r'branch-address',branchAddress)
router.register(r'branch-contact',branchContact)
router.register(r'device-master',DeviceMasterTable)
router.register(r'device-part',device_part)
router.register(r'device-location',device_location_table)
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include('ajeevi_app.urls')),
    path('api/', include(router.urls))
   
]
