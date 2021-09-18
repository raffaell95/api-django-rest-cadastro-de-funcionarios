from rest_framework import viewsets
from .serializers import DepartmentsSerializer
from .models import Department


class DepartmentViewSet(viewsets.ModelViewSet):
    """List, create, remove and update departments"""
    queryset = Department.objects.all()
    serializer_class = DepartmentsSerializer