from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers
from apps.users.serializers import UserDetailsSerializer, UserRegisterSerializer
from apps.students.models import Students


class StudentSerializer(CountryFieldMixin, serializers.ModelSerializer):
    """
    A student serializer to return the student details
    """
    user = UserDetailsSerializer(required=True)

    class Meta:
        model = Students
        fields = ('id',
        'user',
        'UID',
        'parent_id',
        'status',
        'first_name',
        'middle_name',
        'last_name',
        'dob',
        'birthplace',
        'gender',
        'contact_number',
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
        student, created = Students.objects.update_or_create(user=user, **validated_data)
        return student