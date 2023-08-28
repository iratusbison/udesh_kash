from django.shortcuts import render
from rest_framework import viewsets
from .models import Loan, Payment, Investment, Transaction
from .serializers import LoanSerializer, PaymentSerializer, InvestmentSerializer, TransactionSerializer

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    
    def list(self, request, *args, **kwargs):
        loans = self.get_queryset()
        return render(request, 'loans_list.html', {'loans': loans})

    def retrieve(self, request, *args, **kwargs):
        loan = self.get_object()
        return render(request, 'loan_detail.html', {'loan': loan})

    def create(self, request, *args, **kwargs):
        # Handle create logic
        return render(request, 'loan_create.html')
    
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    
    def list(self, request, *args, **kwargs):
        loans = self.get_queryset()
        return render(request, 'payment_list.html', {'loans': loans})

    def retrieve(self, request, *args, **kwargs):
        loan = self.get_object()
        return render(request, 'payment_detail.html', {'loan': loan})

    def create(self, request, *args, **kwargs):
        # Handle create logic
        return render(request, 'payment_create.html')
    
class InvestmentViewSet(viewsets.ModelViewSet):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer
    
    def list(self, request, *args, **kwargs):
        loans = self.get_queryset()
        return render(request, 'investment_list.html', {'loans': loans})

    def retrieve(self, request, *args, **kwargs):
        loan = self.get_object()
        return render(request, 'investment_detail.html', {'loan': loan})

    def create(self, request, *args, **kwargs):
        # Handle create logic
        return render(request, 'investment_create.html')
    
class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    
    def list(self, request, *args, **kwargs):
        loans = self.get_queryset()
        return render(request, 'transaction_list.html', {'loans': loans})

    def retrieve(self, request, *args, **kwargs):
        loan = self.get_object()
        return render(request, 'transaction_detail.html', {'loan': loan})

    def create(self, request, *args, **kwargs):
        # Handle create logic
        return render(request, 'transaction_create.html')
