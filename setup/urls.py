from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from departments.views import DepartmentViewSet
from employees.views import EmployeeViewSet, CreateEmployeeApiView, ActionsEmployeeApiView

router = routers.DefaultRouter()
router.register('departments', DepartmentViewSet, basename='Departments')
router.register('employees', EmployeeViewSet, basename='Employees')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('employees-create', CreateEmployeeApiView.as_view()),
    path('employees-update/<int:pk>', ActionsEmployeeApiView.as_view())
]