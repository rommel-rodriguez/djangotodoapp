"""appconfig URL Configuration

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
from todo import views as todo_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Auth
    path('signup/', todo_views.signupuser, name='signupuser'),
    path('login/', todo_views.loginuser, name='loginuser'),
    path('logout/', todo_views.logoutuser, name='logoutuser'),
    # Todos
    path('', todo_views.hometodos, name='hometodos'),
    path('create/', todo_views.createtodo, name='createtodo'),
    path('current/', todo_views.currenttodos, name='currenttodos'),
    path('todo/<int:todo_pk>', todo_views.viewtodo, name='viewtodo'),
]
