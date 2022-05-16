from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from .models import Bank
from .serializers import BankSerializer

urlpatterns = [
    path('banks/', views.BankList.as_view()),
    path('banks/<int:pk>/', views.BankDetail.as_view()),
    re_path('^banks/user/(?P<id>.+)/$', views.BankUserList.as_view()),
    path('categories/', views.CategoryList.as_view()),
    path('categories/<int:pk>/', views.CategoryDetail.as_view()),
    re_path('^categories/user/(?P<id>.+)/$', views.CategoryUserList.as_view()),
    path('transactions/', views.TransactionList.as_view()),
    path('transactions/<int:pk>/', views.TransactionDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)