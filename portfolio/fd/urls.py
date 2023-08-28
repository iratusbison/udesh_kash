from django.urls import include, path
from . import views


urlpatterns = [
    path( "", views.fixed_deposit_list, name="dashboard"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("base/", views.base , name='base')
]
