from django.urls import path
from . import views

urlpatterns = [
    path('restock/', views.restock_resource, name='restock_resource'),
    path('restock/list/', views.restock_list, name='restock_list'),
]
