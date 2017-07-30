"""aPage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from Home import views as home_view
from django.contrib.auth import login,urls,views

urlpatterns = [
    url(r'^$',home_view.index, ),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$',views.login,{'template_name':'login.html'}),
    url(r'^accounts/register/$',views.logout,{'template_name':'create-account.html'})
]