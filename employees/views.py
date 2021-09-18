from rest_framework import viewsets, generics
from .serializers import *
from .models import Employee

class EmployeeViewSet(viewsets.ModelViewSet):
    """Listing all employees"""
    http_method_names = ['get', 'delete']
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class CreateEmployeeApiView(generics.CreateAPIView):
    """Create a New Employee"""
    serializer_class = EmployeeActionsSerializer

class ActionsEmployeeApiView(generics.RetrieveUpdateAPIView):
    """Update information for an existing employee"""
    def get_queryset(self):
        queryset = Employee.objects.filter(id=self.kwargs['pk'])
        return queryset
    serializer_class = EmployeeActionsSerializer