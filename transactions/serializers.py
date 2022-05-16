from rest_framework import serializers
from .models import Bank, Category, Transaction

class BankSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bank
        fields = ['id', 'name', 'amount', 'created_at', 'properties', 'user']

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_at', 'user']

class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ['id', 'type', 'amount', 'description', 'is_paid', 'payment_method', 'payment_date', 'created_at', 'properties', 'category', 'bank']