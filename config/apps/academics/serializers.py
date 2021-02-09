from apps.academics.models import Level, Section, Session
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


class LevelSerializer(serializers.ModelSerializer):
    """
    A level serializer to return the level details
    """
    session = SessionSerializer(read_only=True)

    class Meta:
        model = Level
        fields = ('id',
                  'name',
                  'description',
                  'order_number',
                  'session')

    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of level
        :return: returns a successfully created level record
        """
        try:
            session_id = validated_data.pop('session')
            session = Session.objects.get(id=session_id)
        except:
            return None
        level = Level.objects.create(session=session, **validated_data)
        return level


class SectionSerializer(serializers.ModelSerializer):
    """
    A section serializer to return the section details
    """
    level = LevelSerializer(read_only=True)

    class Meta:
        model = Section
        fields = ('id',
                  'name',
                  'description',
                  'order_number',
                  'level')

    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of section
        :return: returns a successfully created section record
        """
        try:
            level_id = validated_data.pop('level')
            level = Level.objects.get(id=level_id)
        except:
            return None
        section = Section.objects.create(level=level, **validated_data)
        return level
