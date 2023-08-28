from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('replenishment-orders/', views.replenishment_order_list, name='replenishment_order_list'),
    path('create-replenishment-order/', views.create_replenishment_order, name='create_replenishment_order'),
    path('accounts/login/',views.login_view, name='login'),
    path('loginn/',views.get_redirect_url, name='urlget'),
    path('profile',views.profile_detail,name = 'profile'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
