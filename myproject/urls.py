"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import *

from django.urls import path

from newapp.views import *

from django.contrib.auth import views as auth_views

# This two if you want to enable the Django Admin: (recommended)
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url('admin/', admin.site.urls),
    url('home', home,name="home"),
    # url('/', login,name="login"),
    path("register", register, name="register"),
    path("login", login, name="login"),
    path("logout", logout, name="logout"),
    path('chartsform/', chartsform, name='chartsform'),
    path('delete', delete, name='delete'),
    path('ajax-load/', load_charts, name='ajax_load'),
    path('ajax-load1/', ajax_delete, name='ajax_load1'),
    path('upload/', upload, name='upload'),
    path('UploadSuccess/', UploadSuccess, name='UploadSuccess'),
    path('ajax/load_week_charts',load_week_charts,name='load_week_charts'),
    path('ajax/load_week_upload',load_week_upload,name='load_week_upload'),

]

