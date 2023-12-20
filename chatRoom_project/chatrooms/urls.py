from django.urls import path
from . import views

urlpatterns =[
    # path('',views.index),
    path('login/',views.LoginView.as_view(),name='login'),
    path('signup/',views.SignupView.as_view(),name='signup'),
    path('home',views.HomeView.as_view(),name='home'),
    path('new/',views.CreateRoomView.as_view(),name='new_room'),
    path('<str:room_name>/',views.ChatRoomView.as_view(),name='chat_room'),
    
    
]