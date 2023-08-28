from datetime import timedelta
from django.db import models

class FixedDeposit(models.Model):
    account_number = models.CharField(max_length=20, unique=True)
    account_holder = models.CharField(max_length=100)
    principal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    Date_of_Opening = models.DateField(null=True)
    maturity_date = models.DateField(null=True)
    maturity_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, editable= False)
    maturity_plus_principal_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, editable= False)

    def save(self, *args, **kwargs):
        if self.principal_amount is not None and self.interest_rate is not None and self.maturity_date is not None:
            interest_amount = self.principal_amount * (self.interest_rate / 100)
            self.maturity_amount = self.principal_amount + interest_amount
            self.maturity_plus_principal_amount = self.maturity_amount + self.principal_amount
        super().save(*args, **kwargs)

    def __str__(self):
        return self.account_number

class Stock(models.Model):
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.symbol

class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    stocks = models.ManyToManyField(Stock, through='PortfolioStock')

    def __str__(self):
        return self.name

class PortfolioStock(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateField()

    def __str__(self):
        return f"{self.portfolio.name} - {self.stock.symbol}"
