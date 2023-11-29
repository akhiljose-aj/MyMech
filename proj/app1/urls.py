"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
    path('admin/', admin.site.urls),
    path('',views.home),
    path('abt',views.abt),
    path('services',views.services),
    path('contact',views.con),
    path('log',views.log),
    path('signupusr',views.signupuser),
    path('signupmech',views.signupmech),
    path('profile',views.profile),
    path('home',views.home2),
    path('mhome',views.mech_home),
    path('contact2',views.contact2),
    path('login',views.login),
    path('logout',views.logout),
    path('book',views.book),
    path('bk_service',views.bk_service),
    path('bk_service1',views.bk_service1),
    path('mhome_accept/<int:name>',views.accept_service),
    path('work_complete/<int:name>',views.work_complete),
    path('adminlog',views.adminlog),
    path('login_admin',views.login_admin),
    path('admin_prof',views.admin_profile),
    path('logout_admin',views.logout_admin),
    path('admin_contact',views.admin_con),
    path('download/<f_name>', views.download_file),
    path('reject_mech/<int:name>',views.reject_mech),
    path('acc_mech/<int:id>',views.acc_mech),
    path('delete_mech',views.del_mech),
    path('mech_del',views.mech_del),
    path('user_contact',views.user_contactfun),
    path('responded/<int:name>',views.responded),
    path('mech_contact1',views.mech_contactfun),
    path('mech_responded/<int:name>',views.mech_responded),
    path('update_mech',views.update_mech),
    path('mech_update',views.mech_update),
    path('usrbk_details',views.usrbk_details),
    path('cancel_work/<int:id>',views.cancel_work),
    path('rebook/<int:id>',views.rebook),
]
