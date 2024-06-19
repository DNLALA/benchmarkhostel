from rest_framework import generics
from rest_framework.permissions import AllowAny
from users.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from users.api.serializers import StudentRegistrationSerializer, StudentLoginSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated

class StudentRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = StudentRegistrationSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        return Response(data)

class StudentLoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = StudentLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        token_data = serializer.save()
        return Response(token_data)
    
class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user