

from django.urls import path,include
from . import views
from students.api.views import StudentView
from rest_framework import routers
router = routers.DefaultRouter()
router.register('students',StudentView)
urlpatterns = [
    path('api/', include(router.urls)),


    path('', views.student_list, name='student'),
    path('addstu/', views.add_student, name='add_stu'),
    path('editstu/<int:sid>', views.edit_student, name='edit_stu'),
    path('viewstu/', views.view_student, name='viewstu'),
]
