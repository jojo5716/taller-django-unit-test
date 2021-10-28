# Running test

python manage.py test --pattern="tests_*.py"

# Url to generate random number 
https://csrng.net/csrng/csrng.php?min=0&max=100

# Steps

# 1.- Create python virtual enviroment

## 2.- Install dependencies
```bash
pip install django
pip install djangorestframework
```

## 3.- Create django project
```bash
django-admin startproject taller_unit_test
```

## 4.- Create offer apps
```bash
mkdir apps
cd apps
django-admin startapp offer
```

## 5.- Configure django apps


## 6.- Run app to chceck if it work

## 7.- Create Offer model

## 8.- Create Offer list view
```python
from rest_framework import viewsets

from .models import Offer

class OfferView(viewsets.ModelViewSet):
    queryset = Offer.objects.filter(is_active=True)
```
## 9.- Create Offer serializer

## 10.- Add Offer url

## 11.- Check http://127.0.0.1:8000/offers/

## 12.- Create Offer service (List)

## 13.- Create Offer service (Create)

## 13.- Create Price calculator service
