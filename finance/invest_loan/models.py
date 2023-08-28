from django.db import models

class User(models.Model):
    name = models.TextField()


class Loan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5,decimal_places=2)
    term = models.IntegerField(default=False)
    approved = models.BooleanField(default=False)

class Payment(models.Model):
    loan = models.ForeignKey(Loan , on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

class Investment(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    date = models.DateField()

class Transaction(models.Model):
    investment = models.ForeignKey(Investment, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    type = models.CharField(max_length=20)
    date = models.DateField()