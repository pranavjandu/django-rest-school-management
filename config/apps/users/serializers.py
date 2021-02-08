from rest_framework import serializers
from apps.users.models import User
from allauth.account.adapter import get_adapter
from django.contrib.auth import authenticate

    

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email',)
        read_only_fields = ('email',)


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def get_cleaned_data(self):
        return {
            'password': self.validated_data.get('password', ''),
            'email': self.validated_data.get('email', ''),
        }
    
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['email'], validated_data['password'])
        return user

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.save()
        adapter.save_user(request, user, self)
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
