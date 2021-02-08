from apps.academics.models import Session
from rest_framework import serializers


class SessionSerializer(serializers.ModelSerializer):
    """
    A session serializer to return the session details
    """
    class Meta:
        model = Session
        fields = ('id',
        'name',
        'description',
        'start_date',
        'end_date',
        'is_active')