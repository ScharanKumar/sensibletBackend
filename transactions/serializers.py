from rest_framework import serializers
from .models import Transaction

class TransactionSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'amount', 'transaction_type', 'status', 'user', 'timestamp']
        read_only_fields = ['id', 'timestamp']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'amount', 'transaction_type', 'status', 'timestamp']
        read_only_fields = ['transaction_id', 'timestamp']
