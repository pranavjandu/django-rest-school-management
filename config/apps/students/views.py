from django.shortcuts import render

from apps.students.serializers import *
from apps.students.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class StudentListView(APIView):
    """
    A class based view for creating and fetching student records
    """
    def get(self, format=None):
        """
        Get all the student records
        :param format: Format of the student records to return to
        :return: Returns a list of student records
        """
        students = Students.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a student record
        :param format: Format of the student records to return to
        :param request: Request object for creating student
        :return: Returns a student record
        """
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)

class StudentDetailView(APIView):
    def get(self, request, id, format=None):
        """
        Get the student record for given id
        :param format: Format of the student records to return to
        :return: Returns a list of student records
        """
        try:
            student = Students.objects.get(id=id)
        except:
            error = {'error':'Student with given id not found.'}
            return Response(error, status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(student)
        return Response(serializer.data)


