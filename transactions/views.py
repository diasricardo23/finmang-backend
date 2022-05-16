from .models import Bank, Category, Transaction
from .serializers import BankSerializer, CategorySerializer, TransactionSerializer
from rest_framework import generics
from rest_framework.response import Response

# ---------------------- BANK VIEWS ----------------------
class BankList(generics.ListCreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class BankUserList(generics.ListAPIView):
    serializer_class = BankSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        user_id = self.kwargs['id']
        return Bank.objects.filter(user=user_id)


class BankDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

# ---------------------- CATEGORY VIEWS ----------------------
class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryUserList(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        user_id = self.kwargs['id']
        return Category.objects.filter(user=user_id)

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# ---------------------- TRANSACTION VIEWS ----------------------
class TransactionList(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer