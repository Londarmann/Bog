from rest_framework import serializers
from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


class PurchasesSerializer(serializers.ModelSerializer):
    total_purchases = serializers.IntegerField()
    purchase_date = serializers.DateField()

    class Meta:
        model = Transaction
        fields = ['total_purchases', 'purchase_date']
