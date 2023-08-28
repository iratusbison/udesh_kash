from django.urls import path
from . import views

urlpatterns = [
    path('supply/', views.supply_resource, name='supply_resource'),
    path('supply/list/', views.supply_list, name='supply_list'),
]
