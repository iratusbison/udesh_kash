from django.urls import path
from bot1.views import chat_view

urlpatterns=[
    path('', chat_view, name='chat_view')
]