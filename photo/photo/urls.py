"""config URL Configuration

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

from django.urls import path,include
from . import views
from photo import photo

urlpatterns = [
    # http://127.0.0.1:8000/photo/ : 전체 사진 보기
    path('', views.photo_list, name='photo_list'),

    # http://127.0.0.1:8000/photo/
    path('new/', views.photo_post, name='photo_post'),

    path('<int:pk>/',views.photo_detail, name="photo_detail"),

    path('<int:pk>/remove/', views.views.photo_remove, name="photo_remove"),

    # http://127.0.0.1:8000/photo/1/edit

]
