# Bog app

Transaction Api

## Installation
```bash
pip install -r requirements.txt
```

## Crete project
```
python -m venv venv
source venv/bin/activate
python manage.py makemigration
python manage.py migrate
```

## Run project
```

python manage.py runserver

```

## Insert information into database
To insert data you should place "transaction_data.csv" into bog directory
after that just use command below

```
python manage.py import
```

