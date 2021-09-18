from rest_framework import viewsets, filters
from django_filters.rest_framework import  DjangoFilterBackend
from .serializers import DepartmentsSerializer
from .models import Department


class DepartmentViewSet(viewsets.ModelViewSet):
    """List, create, remove and update departments"""
    queryset = Department.objects.all()
    serializer_class = DepartmentsSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name']
    ordering = ['name']
    search_fields = ['name']