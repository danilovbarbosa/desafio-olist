from django.db import models
from django.db.models import CASCADE


class Address(models.Model):
    '''
    TODO: to implement complete address;
    '''
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=200)
    number = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=10)

class Seller(models.Model):
    fantasy_name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=150)
    phone = models.CharField(max_length=15)
    complete_address = models.ForeignKey(Address, on_delete=models.CASCADE)




