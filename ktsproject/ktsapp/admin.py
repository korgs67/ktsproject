from django.contrib import admin
from .models import Noutbuk

class NoutbukAdmin(admin.ModelAdmin):
    list_display = ['id', 'price', 'description']
    list_display_links = ['id', ]
    search_fields = ['id', 'price', 'description']
    list_editable = ['price']
    list_filter = ['price']

admin.site.register(Noutbuk, NoutbukAdmin)


