from django.contrib import admin

from wish_list.models import WishList


@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    list_display = ('user', 'product')

