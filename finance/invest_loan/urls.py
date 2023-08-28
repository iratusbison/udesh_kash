from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoanViewSet, PaymentViewSet, InvestmentViewSet, TransactionViewSet

router = DefaultRouter()
router.register('loans', LoanViewSet)
router.register('payments',PaymentViewSet)
router.register('investment',InvestmentViewSet)
router.register('transactions', TransactionViewSet)

urlpatterns = [
    path('',include(router.urls)),
]