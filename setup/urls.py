from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from departments.views import DepartmentViewSet
from employees.views import EmployeeViewSet, CreateEmployeeApiView, UpdateAndDeleteEmployeeApiView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView 

router = routers.DefaultRouter()
router.register('departments', DepartmentViewSet, basename='Departments')
router.register('employees', EmployeeViewSet, basename='Employees')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('employees-create', CreateEmployeeApiView.as_view(), name='employees_create'),
    path('employees-actions/<int:pk>', UpdateAndDeleteEmployeeApiView.as_view(), name='employees_actions'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]