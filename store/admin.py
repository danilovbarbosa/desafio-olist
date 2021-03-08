from django.contrib import admin

from store.models import Seller, Address, Categorie, Product, Marketplace


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['zip_code', ]
    search_fields = ['country', 'state', 'city', 'street', 'zip_code', ]


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ['fantasy_name', ]
    search_fields = ['fantasy_name', ]

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ['name', ]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'value', ]
    search_fields = ['name', 'description', 'value']
    list_filter = ['categories',]


@admin.register(Marketplace)
class MarketplaceAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name', ]
