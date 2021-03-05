from django.db import models

class Seller(models.Model):
    fantasy_name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=150)
    phone = models.CharField(max_length=15)


