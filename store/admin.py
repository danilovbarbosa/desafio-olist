from django.contrib import admin

from store.models import Seller, Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['zip_code', ]


