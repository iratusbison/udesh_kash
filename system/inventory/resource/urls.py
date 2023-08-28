from django.urls import path
from . import views

urlpatterns = [
    path('products/',views.product_list, name ='product_list'),
    path('product/create/',views.create_product, name ='create_product'),
    path('product/<int:pk>/update/',views.update_product, name ='update_product'),
    path('product/<int:pk>/delete',views.delete_product, name ='delete_product'),

]