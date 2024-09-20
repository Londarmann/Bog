from django.db import models

# Create your models here.

from django.db import models


class Transaction(models.Model):
    user_id = models.IntegerField()
    transaction_id = models.CharField(max_length=255, unique=True)
    transaction_time = models.DateTimeField()
    item_code = models.IntegerField()
    item_description = models.CharField(max_length=255)
    number_of_items_purchased = models.IntegerField()
    cost_per_item = models.DecimalField(max_digits=10, decimal_places=2)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"Transaction {self.transaction_id}: User {self.user_id}, Item {self.item_code}"
