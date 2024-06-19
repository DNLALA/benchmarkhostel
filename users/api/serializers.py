from rest_framework import serializers
from users.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'username', 'reg_no', 'email', 'is_student', 'is_warden',
            'is_active', 'created_at', 'last_login', 'tokens', 'has_hostel', 'gender'
        ]
        read_only_fields = ['id', 'created_at', 'last_login', 'tokens']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user


class StudentRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'reg_no', 'password', 'password2', 'gender']
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        validated_data['is_student'] = True
        user = User.objects.create_user(**validated_data)
        token, created = Token.objects.get_or_create(user=user)
        return {'token': token.key}
    
class StudentLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)

            if not user:
                raise serializers.ValidationError("Invalid login credentials")
            if not user.is_student:
                raise serializers.ValidationError("Only students can log in here")

        else:
            raise serializers.ValidationError("Must include both email and password")

        data['user'] = user
        return data

    def create(self, validated_data):
        user = validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return {'token': token.key}
    
class WardenRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'reg_no', 'password', 'password2', 'gender']
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        validated_data['is_warden'] = True
        user = User.objects.create_user(**validated_data)
        token, created = Token.objects.get_or_create(user=user)
        return {'token': token.key}
    
class WardenLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)

            if not user:
                raise serializers.ValidationError("Invalid login credentials")
            if not user.is_warden:
                raise serializers.ValidationError("Only wardens can log in here")

        else:
            raise serializers.ValidationError("Must include both email and password")

        data['user'] = user
        return data

    def create(self, validated_data):
        user = validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return {'token': token.key}