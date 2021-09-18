from django.contrib import admin
from .models import Department


class Departments(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

admin.site.register(Department, Departments)
