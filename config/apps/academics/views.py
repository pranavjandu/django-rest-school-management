from django.shortcuts import render

from apps.academics.serializers import *
from apps.academics.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class SessionListView(APIView):
    """
    A class based view for creating and fetching session records
    """

    def get(self, format=None):
        """
        Get all the session records
        :param format: Format of the session records to return to
        :return: Returns a list of session records
        """
        sessions = Session.objects.all()
        serializer = SessionSerializer(sessions, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a session record
        :param format: Format of the session records to return to
        :param request: Request object for creating session
        :return: Returns a session record
        """
        serializer = SessionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)


class SessionDetailView(APIView):
    def get(self, request, id, format=None):
        """
        Get the session record for given id
        :param format: Format of the session records to return to
        :return: Returns a list of session records
        """
        try:
            session = Session.objects.get(id=id)
        except:
            error = {'error': 'Session with given id not found.'}
            return Response(error, status=status.HTTP_404_NOT_FOUND)
        serializer = SessionSerializer(session)
        return Response(serializer.data)


class ActiveSessionView(APIView):
    def get(self, request, format=None):
        """
        Get the session record for the active session
        :param format: Format of the session records to return to
        :return: Returns a session records
        """
        session = Session.objects.filter(is_active=True)
        serializer = SessionSerializer(session, many=True)
        return Response(serializer.data)


class ActivateSessionView(APIView):
    def get(self, request, id, format=None):
        """
        Activate the session for the given session id and deactivate for the previous active session
        :param format: Format of the session records to return to
        :return: Returns the active session
        """
        try:
            session = Session.objects.get(id=id)
        except:
            error = {'error': 'Session with given id not found.'}
            return Response(error, status=status.HTTP_404_NOT_FOUND)
        prev_session = Session.objects.filter(is_active=True)
        for x in prev_session:
            x.is_active = False
            x.save()
        session.is_active = True
        session.save()
        serializer = SessionSerializer(session)
        return Response(serializer.data)


class LevelListView(APIView):
    def get(self, format=None):
        """
        Get all the level records
        :param format: Format of the level records to return to
        :return: Returns a list of level records
        """
        levels = Level.objects.all()
        serializer = LevelSerializer(levels, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a level record
        :param format: Format of the level records to return to
        :param request: Request object for creating level
        :return: Returns a level record
        """
        serializer = LevelSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            level = serializer.create(validated_data=request.data)
            if level is None:
                error = {'error': 'Session with given id not found.'}
                return Response(error,
                                status=status.HTTP_400_BAD_REQUEST)
            level_serializer = LevelSerializer(level)
            return Response(level_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)


class LevelBySessionView(APIView):
    def get(self, request, id, format=None):
        """
        Get all the level records by session id
        :param format: Format of the level records to return to
        :return: Returns a list of level records
        """
        try:
            session = Session.objects.get(id=id)
        except:
            error = {'error': 'Session with given id not found.'}
            return Response(error,
                            status=status.HTTP_400_BAD_REQUEST)
        levels = Level.objects.filter(session=session)
        serializer = LevelSerializer(levels, many=True)
        return Response(serializer.data)


class LevelDetailView(APIView):
    def get(self, request, id, format=None):
        """
        Get the level records by id
        :param format: Format of the level record to return to
        :return: Returns a level record
        """
        try:
            level = Level.objects.get(id=id)
        except:
            error = {'error': 'Level with given id not found.'}
            return Response(error,
                            status=status.HTTP_400_BAD_REQUEST)
        serializer = LevelSerializer(level)
        return Response(serializer.data)


class SectionListView(APIView):
    def get(self, format=None):
        """
        Get all the section records
        :param format: Format of the section records to return to
        :return: Returns a list of section records
        """
        sections = Section.objects.all()
        serializer = SectionSerializer(sections, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a section record
        :param format: Format of the section records to return to
        :param request: Request object for creating section
        :return: Returns a section record
        """
        serializer = SectionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            section = serializer.create(validated_data=request.data)
            if section is None:
                error = {'error': 'Level with given id not found.'}
                return Response(error,
                                status=status.HTTP_400_BAD_REQUEST)
            section_serializer = SectionSerializer(section)
            return Response(section_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)


class SectionByLevelView(APIView):
    def get(self, request, id, format=None):
        """
        Get all the section records by level id
        :param format: Format of the section records to return to
        :return: Returns a list of section records
        """
        try:
            level = Level.objects.get(id=id)
        except:
            error = {'error': 'Level with given id not found.'}
            return Response(error,
                            status=status.HTTP_400_BAD_REQUEST)
        sections = Section.objects.filter(level=level)
        serializer = SectionSerializer(sections, many=True)
        return Response(serializer.data)


class SectionDetailView(APIView):
    def get(self, request, id, format=None):
        """
        Get the section records by id
        :param format: Format of the section records to return to
        :return: Returns a section record
        """
        try:
            section = Section.objects.get(id=id)
        except:
            error = {'error': 'Section with given id not found.'}
            return Response(error,
                            status=status.HTTP_400_BAD_REQUEST)
        serializer = SectionSerializer(section)
        return Response(serializer.data)


class ClassListView(APIView):
    def get(self, format=None):
        """
        Get all the class records
        :param format: Format of the class records to return to
        :return: Returns a list of class records
        """
        classes = Class.objects.all()
        serializer = ClassSerializer(classes, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a class record
        :param format: Format of the class records to return to
        :param request: Request object for creating class
        :return: Returns a class record
        """
        serializer = ClassSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            classx = serializer.create(validated_data=request.data)
            if classx is None:
                error = {'error': 'Section with given id not found.'}
                return Response(error,
                                status=status.HTTP_400_BAD_REQUEST)
            class_serializer = ClassSerializer(classx)
            return Response(class_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)


class ClassBySectionView(APIView):
    def get(self, request, id, format=None):
        """
        Get all the class records by section id
        :param format: Format of the class records to return to
        :return: Returns a list of class records
        """
        try:
            section = Section.objects.get(id=id)
        except:
            error = {'error': 'Section with given id not found.'}
            return Response(error,
                            status=status.HTTP_400_BAD_REQUEST)
        classes = Class.objects.filter(section=section)
        serializer = ClassSerializer(classes, many=True)
        return Response(serializer.data)

class ClassDetailView(APIView):
    def get(self, request, id, format=None):
        """
        Get the class records by id
        :param format: Format of the class records to return to
        :return: Returns a class record
        """
        try:
            class_obj = Class.objects.get(id=id)
        except:
            error = {'error': 'Class with given id not found.'}
            return Response(error,
                            status=status.HTTP_400_BAD_REQUEST)
        serializer = ClassSerializer(class_obj)
        return Response(serializer.data)

class ClassStudentsView(APIView):
    def get(self, request, id, format=None):
        """
        Get the class-student tree records by class id
        :param format: Format of the class records to return to
        :return: Returns a class record
        """
        try:
            class_obj = Class.objects.get(id=id)
        except:
            error = {'error': 'Class with given id not found.'}
            return Response(error,
                            status=status.HTTP_400_BAD_REQUEST)
        serializer = ClassWithStudentsSerializer(class_obj)
        return Response(serializer.data)

class ClassSubjectView(APIView):
    def get(self, request, id, format=None):
        """
        Get the class-subject tree records by class id
        :param format: Format of the class records to return to
        :return: Returns a class record
        """
        try:
            class_obj = Class.objects.get(id=id)
        except:
            error = {'error': 'Class with given id not found.'}
            return Response(error,
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            classsubject_objects = class_obj.classsubjects
        except:
            error = {'error': 'Error in retrieving class-subjects'}
            return Response(error,
                            status=status.HTTP_400_BAD_REQUEST)           
        serializer = ClassSubjectSerializer(classsubject_objects, many=True)
        return Response(serializer.data)


class ClassSubjectListView(APIView):
    def get(self, format=None):
        """
        Get all the classsubject records
        :param format: Format of the classsubject records to return to
        :return: Returns a list of classsubject records
        """
        classsubjects = ClassSubject.objects.all()
        serializer = ClassSerializer(classsubjects, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a classsubject record
        :param format: Format of the classsubject records to return to
        :param request: Request object for creating classsubject
        :return: Returns a classsubject record
        """
        serializer = ClassSubjectSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            classsubject = serializer.create(validated_data=request.data)
            if classsubject is None:
                error = {'error': 'Error in creating the class-subject'}
                return Response(error,
                                status=status.HTTP_400_BAD_REQUEST)
            classsubject_serializer = ClassSubjectSerializer(classsubject)
            return Response(classsubject_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)

class SubjectListView(APIView):
    def get(self, format=None):
        """
        Get all the subject records
        :param format: Format of the subject records to return to
        :return: Returns a list of subject records
        """
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a subject record
        :param format: Format of the subject records to return to
        :param request: Request object for creating subject
        :return: Returns a subject record
        """
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            subject = serializer.create(validated_data=request.data)
            if subject is None:
                error = {'error': 'Section with given id not found.'}
                return Response(error,
                                status=status.HTTP_400_BAD_REQUEST)
            subject_serializer = SubjectSerializer(subject)
            return Response(subject_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)


class SubjectDetailView(APIView):
    def get(self, request, id, format=None):
        """
        Get the subject  records by id
        :param format: Format of the subject  records to return to
        :return: Returns a subject  record
        """
        try:
            subject_obj = Subject.objects.get(id=id)
        except:
            error = {'error': 'Subject with given id not found.'}
            return Response(error,
                            status=status.HTTP_400_BAD_REQUEST)
        serializer = SubjectSerializer(subject_obj)
        return Response(serializer.data)


class ClassTeacherView(APIView):
    def get(self, request, id, format=None):
        """
        Get the class-teacher tree records by class id
        :param format: Format of the class records to return to
        :return: Returns a class record
        """
        try:
            class_obj = Class.objects.get(id=id)
        except:
            error = {'error': 'Class with given id not found.'}
            return Response(error,
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            classsubject_objects = class_obj.classsubjects
        except:
            error = {'error': 'Error in retrieving class-subjects'}
            return Response(error,
                            status=status.HTTP_400_BAD_REQUEST)           
        serializer = ClassSubjectSerializer(classsubject_objects, many=True)
        return Response(serializer.data)