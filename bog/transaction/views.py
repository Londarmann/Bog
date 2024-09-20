from django.db.models.functions import TruncDay, TruncDate
from rest_framework import generics

from django.db.models import Sum
from rest_framework.pagination import PageNumberPagination

from .models import Transaction
from .serializers import TransactionSerializer, PurchasesSerializer


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10

class TransactionListView(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    pagination_class = CustomPageNumberPagination

class UserPurchasesView(generics.ListAPIView):
    serializer_class = PurchasesSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return (
            Transaction.objects.filter(user_id=user_id)
            .annotate(purchase_date=TruncDate('transaction_time'))
            .values('purchase_date')
            .annotate(total_purchases=Sum('number_of_items_purchased'))
            .order_by('purchase_date')

        )


class ProductPurchasesView(generics.ListAPIView):
    serializer_class = PurchasesSerializer
    def get_queryset(self):
        item_code = self.kwargs['item_code']
        return (
            Transaction.objects.filter(item_code=item_code)
            .annotate(purchase_date=TruncDate('transaction_time'))
            .values('purchase_date')
            .annotate(total_purchases=Sum('number_of_items_purchased'))
            .order_by('purchase_date')

        )





