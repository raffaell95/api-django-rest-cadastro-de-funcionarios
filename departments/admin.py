from django.contrib import admin
from django.db.models.functions import Lower

from .models import Department


class Departments(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', )
    list_per_page = 10
    ordering = ('name',)

admin.site.register(Department, Departments)
