import os
from pathlib import Path

import pandas as pd
from django.core.management.base import BaseCommand

from transaction.models import Transaction


class Command(BaseCommand):
    help = "Start the import of Transactions from a CSV file"

    def handle(self, *args, **kwargs):
        current_dir = Path(__file__)

        project_dir = [p for p in current_dir.parents if p.parts[-1] == 'bog'][0]

        file_name = os.path.join(project_dir, 'transaction_data.csv')

        df = pd.read_csv(file_name)

        df.dropna(inplace=True)
        df.drop_duplicates(subset=['TransactionId'], inplace=True)

        transactions = []
        for index, row in df.iterrows():
            transaction_time_str = row['TransactionTime'].replace('IST', '').strip()
            transaction_time = pd.to_datetime(transaction_time_str, format='%a %b %d %H:%M:%S %Y')

            transactions.append(Transaction(
                user_id=row['UserId'],
                transaction_id=row['TransactionId'],
                transaction_time=transaction_time,
                item_code=row['ItemCode'],
                item_description=row['ItemDescription'],
                number_of_items_purchased=row['NumberOfItemsPurchased'],
                cost_per_item=row['CostPerItem'],
                country=row['Country']
            ))

        try:
            Transaction.objects.bulk_create(transactions)
            self.stdout.write(self.style.SUCCESS('Successfully imported transactions'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'{e}'))
