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
            error = {'error':'Session with given id not found.'}
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
        serializer = SessionSerializer(session,many=True)
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
            error = {'error':'Session with given id not found.'}
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
                error = {'error':'Session with given id not found.'}
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
            error = {'error':'Session with given id not found.'}
            return Response(error,
                        status=status.HTTP_400_BAD_REQUEST)
        levels = Level.objects.filter(session=session)
        serializer = LevelSerializer(levels, many=True)
        return Response(serializer.data)


class LevelDetailView(APIView):
    def get(self, request, id, format=None):
        """
        Get all the level records by level id
        :param format: Format of the level records to return to
        :return: Returns a list of level records
        """
        try:
            level = Level.objects.get(id=id)
        except:
            error = {'error':'Level with given id not found.'}
            return Response(error,
                        status=status.HTTP_400_BAD_REQUEST)
        serializer = LevelSerializer(level)
        return Response(serializer.data)