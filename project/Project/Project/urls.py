"""Project URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/signup/',views.signup, name="signup" ),
    path('registration/login/', views.login, name="login"),
    path('registration/logout', views.logout, name="logout"),
    
    # path('board/',views.board, name='board'),
    # path('board/board_detail/<int:pk>', views.board_detail, name='board_detail'),
    path('', views.home, name = "home"),
    path('memberCheck', views.memberCheck, name = "memberCheck"),
    path('board_notice',views.board_notice, name = 'board_notice'),
    path('board_session', views.board_session, name = 'board_session'),
    path('board_session/detail/<int:pk>', views.session_detail, name = 'session_detail'),
    path('board_notice/detail/<int:pk>',views.notice_detail, name = 'notice_detail'),
    path('board_notice/edit/<int:pk>',views.notice_edit, name = 'notice_edit'),
    path('board_notice/new',views.notice_new,name="notice_new"),
    path('board_session/new',views.session_new,name="session_new"),
    path("about", views.about, name = "about"),
    path("activities", views.activities, name = "activities"),
    path("joinUS", views.joinUs, name = "joinUs"),
    path('mypage', views.myPage, name ="mypage"),
    path('board_notice', views.board_notice, name ="board_notice")
]
