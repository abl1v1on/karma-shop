from django.contrib import admin

from .models import Contact, Newsletter


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', )


@admin.register(Newsletter)
class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ('subject', 'text')
