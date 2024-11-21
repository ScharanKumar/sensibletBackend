from django.shortcuts import render, HttpResponse

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView
from .models import Transaction
from .serializers import TransactionSerializer, TransactionSerializer1
# core/views.py
from django.http import JsonResponse
from .utils import get_user_id_by_username

def fetch_user_id(request, username):
    # Call the function to get the user ID
    user_id = get_user_id_by_username(username)

    if user_id == "User not found":
        return JsonResponse({"error": user_id}, status=404)

    return JsonResponse({"user_id": user_id})


class CreateTransactionOrGetAllTransactionsView(APIView):
    # done
    def post(self, request):
        serializer = TransactionSerializer1(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"transactionCreated":serializer.data,"message":"Transaction is successfully created!"}, status=status.HTTP_201_CREATED)
        return Response({"error":"Transaction creation failed, please enter all fields.","message":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

    # done
    def get(self, request):
        user_id = request.query_params.get('user_id')
        if not user_id:
            return Response({'error': 'user_id is required'}, status=status.HTTP_400_BAD_REQUEST)
        transactions = Transaction.objects.filter(user_id=user_id)
        serializer = TransactionSerializer(transactions, many=True)
        return Response({'transactions': serializer.data,'message':'Fetched user transactions successfully!'}, status=status.HTTP_200_OK)


class TransactionUpdateOrGetATransactionDetailsView(APIView):
    # done
    def get(self, request, transaction_id):
        try:
            transaction = Transaction.objects.get(id=transaction_id)
        except Transaction.DoesNotExist:
            return Response({'error': 'Transaction not found for fetching transaction details.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = TransactionSerializer(transaction)
        return Response({"transactionDetails":serializer.data,"message":"Transaction details fetched successfully!"}, status=status.HTTP_200_OK)

    # done
    def put(self, request, transaction_id):
        try:
            transaction = Transaction.objects.get(id=transaction_id)
        except Transaction.DoesNotExist:
            return Response({'error': 'Transaction not found for updating transaction status.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = TransactionSerializer(transaction, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"updatedTransaction":serializer.data,"message":"Transaction updated successfully!"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def index(request):
    context ={
        "variable":{'this is sent'}
    }
    return render(request,"index.html", context)

def about(request):
    return HttpResponse("THIS IS about page")