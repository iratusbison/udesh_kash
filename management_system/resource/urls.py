
from .inventory.views import product_list
from .staff.views import staff_login , staff_profile
from django.urls import include, path


urlpatterns = [
    path('',product_list,name='product'),
    path('p', staff_profile, name='profile'),
    #path('log', Staffs, name='log'),
    path('login/', staff_login, name='staff_login'),
]
