
from rest_framework import viewsets

from students.models import Student
from .serializers import StudentSerializer
class StudentView(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()