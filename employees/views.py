from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, filters
from .serializers import *
from .models import Employee

class EmployeeViewSet(viewsets.ModelViewSet):
    """Listing all employees"""
    http_method_names = ['get', 'delete']
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name']
    ordering = ['name']
    search_fields = ['name', 'email']

class CreateEmployeeApiView(generics.CreateAPIView):
    """Create a New Employee"""
    serializer_class = EmployeeActionsSerializer

class ActionsEmployeeApiView(generics.RetrieveUpdateAPIView):
    """Update information for an existing employee"""
    def get_queryset(self):
        queryset = Employee.objects.filter(id=self.kwargs['pk'])
        return queryset
    serializer_class = EmployeeActionsSerializer