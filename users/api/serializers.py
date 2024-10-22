from rest_framework.serializers import ModelSerializer, ValidationError
from ..models import User, Student, StudyCertificate

class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'dni', 'birth_date', 'address', 'password', 'last_name', 'first_name', 'phone']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password != None:
            instance.set_password(password)
        instance.save()
        return instance


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'dni', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'is_authenticated', 'phone']


class UserUpdateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone']   


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'dni', 'birth_date', 'user']


class StudyCertificateSerializer(ModelSerializer):
    class Meta:
        model = StudyCertificate
        fields = ['student', 'certified_file', 'upload_date', 'verification_status']

    def validate_certified_file(self, value):
        if not value.name.endswith('.pdf'):
            raise ValidationError('Only PDF file')
        return value