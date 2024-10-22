from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, mixins, viewsets

from ..models import User, Student, StudyCertificate
from .serializers import StudentSerializer, UserSerializer, UserRegisterSerializer, UserUpdateSerializer, StudyCertificateSerializer

# class StudentModelViewSet(mixins.RetrieveModelMixin,
#                           mixins.ListModelMixin,
#                           viewsets.ModelViewSet):
#     serializer_class = StudentSerializer
#     queryset = Student.objects.all()


class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class StudentAPIView(APIView):
    def post(self, request):
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
    

class StudyCertificateModelViewSet(viewsets.ModelViewSet):
    queryset = StudyCertificate.objects.all()
    serializer_class = StudyCertificateSerializer