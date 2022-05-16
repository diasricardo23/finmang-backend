from unicodedata import category
from django.db import models
from users.models import User

# Create your models here.
class Bank(models.Model):
    name = models.CharField(max_length=128)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    properties = models.JSONField(default=dict, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_at']

class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_at']

class Transaction(models.Model):
    type = models.CharField(max_length=128)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    is_paid = models.BooleanField(default=False)
    payment_method = models.CharField(max_length=128)
    payment_date = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    properties = models.JSONField(default=dict, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)