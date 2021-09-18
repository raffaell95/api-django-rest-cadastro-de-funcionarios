from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    department = serializers.ReadOnlyField(source='department.name')
    class Meta:
        model = Employee
        fields = ['name','email', 'department']


class EmployeeActionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name','email', 'department']