from django.http.request import HttpHeaders
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, filters, request
from .serializers import *
from .models import Employee
from rest_framework.permissions import IsAuthenticated

class EmployeeViewSet(viewsets.ModelViewSet):
    """Listing all employees"""
    http_method_names = ['get']
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name']
    ordering = ['name']
    search_fields = ['name', 'email']
    

class CreateEmployeeApiView(generics.CreateAPIView):
    """Create a New Employee"""
    permission_classes = (IsAuthenticated, )
    serializer_class = EmployeeActionsSerializer

class UpdateAndDeleteEmployeeApiView(generics.RetrieveUpdateDestroyAPIView):
    """Update or delete information for an existing employee"""
    permission_classes = (IsAuthenticated, )
    def get_queryset(self):
        queryset = Employee.objects.filter(id=self.kwargs['pk'])
        return queryset
    serializer_class = EmployeeActionsSerializer