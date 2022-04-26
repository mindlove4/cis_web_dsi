"""web01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from cisweb import views
from loginsystem import views as views_login
from django.conf.urls.static import static, serve
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.urls import re_path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home' ),
    path('login1/', views_login.login_teacher, name='teacher'),
    path('edit_profile/', views.edit_profile, name='edit'),
    path('aadForm', views.profile),
    path('login2/', views_login.login_staff, name='staff'),
    path('login3/', views_login.login_student, name='student'),
    path('home/', views.cishome1,  name='profile'),
    path('student_profile/', views.student_profile, name='student_profile'),
    path('responsibiility/', views.responsibiility, name='res'),
    path('accounts/', include('allauth.urls')),
    path('train/', views.train, name='train'),
    path('train_details/', views.traindetails, name='details'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += staticfiles_urlpatterns()