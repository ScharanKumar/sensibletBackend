from django.contrib import admin
from django.urls import path
from transactions import views
from django.urls import path
from rest_framework.response import Response
from rest_framework.views import APIView
from .views import CreateTransactionOrGetAllTransactionsView,   TransactionUpdateOrGetATransactionDetailsView


class TestView(APIView):
    def get(self, request):
        return Response({"message": "Django REST Framework is working!"})


urlpatterns = [

    path('api/transactions/', CreateTransactionOrGetAllTransactionsView.as_view(), name='create-transaction-or-get-all-transactions'),
    path('api/transactions/<int:transaction_id>/', TransactionUpdateOrGetATransactionDetailsView.as_view(), name='transaction-status-update-or-get-transaction-details'),


    path('', views.index, name='transactions'),
    path('about', views.about, name='about'),
    path('test/', TestView.as_view(), name='test-view'),

    path('user-id/<str:username>/', views.fetch_user_id, name='fetch_user_id'),
]