from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers
from apps.users.serializers import UserDetailsSerializer, UserRegisterSerializer
from apps.teachers.models import Teacher


class TeacherSerializer(CountryFieldMixin, serializers.ModelSerializer):
    """
    A student serializer to return the student details
    """
    user = UserDetailsSerializer(required=True)

    class Meta:
        model = Teacher
        fields = ('id',
        'user',
        'personnel_number',
        'first_name',
        'last_name',
        'dob',
        'birthplace',
        'gender',
        'marital_status',
        'contact_number',
        'alternate_number',
        'nationality',
        'photo',
        'emergency_contact_name',
        'emergency_contact_number',
        'address_line1',
        'address_line2',
        'city',
        'state',
        'zipcode',
        'country')

    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of student
        :return: returns a successfully created student record
        """
        user_data = validated_data.pop('user')
        user = UserRegisterSerializer.create(UserRegisterSerializer(), validated_data=user_data)
        teacher, created = Teacher.objects.update_or_create(user=user, **validated_data)
        return teacher