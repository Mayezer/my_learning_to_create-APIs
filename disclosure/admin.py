from django.contrib import admin
from disclosure.models import Disclosure

@admin.register(Disclosure)
class DisclosureAdmin(admin.ModelAdmin):
    list_display = ['social_network', 'date']
