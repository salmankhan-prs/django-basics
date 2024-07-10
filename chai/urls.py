"""
URL configuration for chaiaurdjango project.

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
from django.urls import path, include
from .views import all_chai ,get_chai_details_by_id,chai_store_view
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', view=all_chai,name="all home"),
    path('<int:chai_id>/',view=get_chai_details_by_id,name="details_by_id"),
    path('chai_stores/',view=chai_store_view,name="chai_stores")
    
]
