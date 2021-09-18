from django.contrib import admin
from .models import Employee

class Employees(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'department')
    list_display_links = ('id', 'name')

admin.site.register(Employee, Employees)
