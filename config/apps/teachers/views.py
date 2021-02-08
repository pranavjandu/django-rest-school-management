from django.shortcuts import render

from apps.teachers.serializers import *
from apps.teachers.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class TeacherListView(APIView):
    """
    A class based view for creating and fetching teacher records
    """
    def get(self, format=None):
        """
        Get all the teacher records
        :param format: Format of the teacher records to return to
        :return: Returns a list of teacher records
        """
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a teacher record
        :param format: Format of the teacher records to return to
        :param request: Request object for creating teacher
        :return: Returns a teacher record
        """
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)

class TeacherDetailView(APIView):
    def get(self, request, id, format=None):
        """
        Get the teacher record for given id
        :param format: Format of the teacher records to return to
        :return: Returns a list of teacher records
        """
        try:
            teacher = Teacher.objects.get(id=id)
        except:
            error = {'error':'teacher with given id not found.'}
            return Response(error, status=status.HTTP_404_NOT_FOUND)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)


