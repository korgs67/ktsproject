from django.contrib import admin
from .models import Noutbuk

class NoutbukAdmin(admin.ModelAdmin):
    list_display = ['id', 'price','parse_datetime', 'description']
    list_display_links = ['id', ]
    search_fields = ['id', 'price','parse_datetime', 'description']
    list_editable = ['price']
    list_filter = ['parse_datetime','price']

admin.site.register(Noutbuk, NoutbukAdmin)


