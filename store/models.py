from django.db import models
from django.db.models import CASCADE


class Address(models.Model):
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=200)
    number = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=10)

    class Meta:
        ordering = ['country']

    def __str__(self):
        return self.street


class Seller(models.Model):
    fantasy_name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=200)
    contact_phone = models.CharField(max_length=15)
    complete_address = models.ForeignKey(Address, on_delete=models.CASCADE)

    class Meta:
        ordering = ['fantasy_name']

    def __str__(self):
        return self.fantasy_name

class Categorie(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    value = models.FloatField()
    categories = models.ManyToManyField(Categorie)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Marketplace(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    site = models.CharField(max_length=200)
    contact_phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=200)
    contact_technical_manager = models.CharField(max_length=15)