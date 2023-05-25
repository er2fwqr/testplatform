"""
URL configuration for lk_test project.

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
from django.urls import path
from test0 import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', auth_views.LoginView.as_view(success_url='/index/'), name='login'),
    path('index/',views.index,name='index'),
    path('test_report/', views.test_report, name='test_report'),
    path('report/', views.test_report, name='report'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('admin/', admin.site.urls),
    path('history_report/',views.history_report,name='history_report'),
    path('history_report_item/<str:report_path>/',views.history_report_item,name='history_report_item')
]

