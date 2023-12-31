from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create/', views.create, name='create'),
    path('your_rooms/', views.your_rooms, name='your_rooms'),
    path('requests', views.join_requests, name='join_requests'),
    path('joinedRooms', views.joined_rooms, name='joined_rooms'),
    path('room/<str:room_name>', views.room, name='room'),

    # API Routes
    path('joinRoom', views.join_room, name='join_room'),
    path('AcceptRequest', views.accept_request, name='accept_request'),
    path('RejectRequest', views.reject_request, name='reject_request'),
    path('sendMessage', views.send_message, name="send_message")
]