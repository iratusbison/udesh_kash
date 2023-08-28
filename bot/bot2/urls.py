from django.urls import path
from bot2.views import ChatView

urlpatterns=[
    path('', ChatView, name='chat')
]