from apps.teachers.models import Teacher
from apps.students.serializers import StudentSerializer
from apps.teachers.serializers import TeacherSerializer
from apps.academics.models import Class, ClassSubject, Level, Section, Session, Subject
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


class ClassSerializer(serializers.ModelSerializer):
    """
    A class serializer to return the class details
    """
    section = SectionSerializer(read_only=True)

    class Meta:
        model = Class
        fields = ('id',
                  'name',
                  'description',
                  'order_number',
                  'section')

    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of class
        :return: returns a successfully created class record
        """
        try:
            section_id = validated_data.pop('section')
            section = Section.objects.get(id=section_id)
        except:
            return None
        classx = Class.objects.create(section=section, **validated_data)
        return classx


class SubjectSerializer(serializers.ModelSerializer):
    """
    A class serializer to return the subject details
    """
    section = SectionSerializer(read_only=True)

    class Meta:
        model = Subject
        fields = ('id',
                  'name',
                  'description',
                  'external_subject_id',
                  'section')

    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of subject
        :return: returns a successfully created subject record
        """
        try:
            section_id = validated_data.pop('section')
            section = Section.objects.get(id=section_id)
        except:
            return None
        subject = Subject.objects.create(section=section, **validated_data)
        return subject

class ClassSubjectSerializer(serializers.ModelSerializer):
    """
    A class serializer to return the class subject details
    """   
    classes = ClassSerializer(read_only=True)
    subject = SubjectSerializer(read_only=True)
    teacher = TeacherSerializer(read_only=True)

    class Meta:
        model = ClassSubject
        fields = ('id',
                  'classes',
                  'subject',
                  'teacher',)

    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of classsubject
        :return: returns a successfully created classsubject record
        """
        try:
            class_id = validated_data.pop('class')
            classx = Class.objects.get(id=class_id)
        except:
            return None
        try:
            subject_id = validated_data.pop('subject')
            subject = Subject.objects.get(id=subject_id)
        except:
            return None
        try:
            teacher_id = validated_data.pop('teacher')
            teacher = Teacher.objects.get(id=teacher_id)
        except:
            return None
        classsubject = ClassSubject.objects.create(classes=classx, subject=subject, teacher=teacher)
        return classsubject
    
class ClassWithStudentsSerializer(serializers.ModelSerializer):
    section = SectionSerializer(read_only=True)
    students = StudentSerializer(read_only=True, many=True)

    class Meta:
        model = Class
        fields = ('id',
                  'name',
                  'description',
                  'order_number',
                  'section',
                  'students')



