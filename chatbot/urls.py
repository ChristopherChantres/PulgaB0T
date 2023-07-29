from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('messages/', views.messages, name='messages'),
  path('api/', views.messages_api, name="messages-api")
]
