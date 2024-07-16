from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from hostel.models import Hostel, Request
from .serializers import HostelSerializer, HostelDetailSerializer, RequestSerializer
from users.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class RequestDetailView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RequestSerializer

    def get(self, request, hostel_id, format=None):
        hostel = get_object_or_404(Hostel, id=hostel_id)
        request_obj = get_object_or_404(Request, user=hostel)
        serializer = RequestSerializer(request_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

class HostelCreateView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = HostelSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data.get('user', None)
            room_number = serializer.validated_data.get('room_number')
            defaults = {k: v for k, v in serializer.validated_data.items() if k != 'room_number'}
            
            if user:
                hostel, created = Hostel.objects.update_or_create(
                    user=user,
                    room_number=room_number,
                    defaults=defaults
                )
            else:
                hostel = Hostel.objects.create(**serializer.validated_data)
                created = True

            return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserHostelDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = HostelDetailSerializer

    def get_object(self):
        user = self.request.user
        try:
            return user.hostel 
        except Hostel.DoesNotExist:
            raise Http404("Hostel not found for this user")

    def get(self, request, format=None):
        hostel = self.get_object()
        serializer = self.serializer_class(hostel)
        return Response(serializer.data)
    
class HostelListView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = HostelDetailSerializer

    def get(self, request, format=None):
        hostels = Hostel.objects.all().order_by('created_at') 
        serializer = self.serializer_class(hostels, many=True)
        return Response(serializer.data)
    
class HostelDetailByUserView(APIView):
    serializer_class = HostelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        try:
            hostel = Hostel.objects.get(user=request.user)
            serializer = HostelSerializer(hostel)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Hostel.DoesNotExist:
            return Response({"error": "Hostel not found for the given user ID"}, status=status.HTTP_404_NOT_FOUND)
        
class ChangeHostelUserView(APIView):
    def put(self, request, hostel_id):
        try:
            hostel = Hostel.objects.get(id=hostel_id)
        except Hostel.DoesNotExist:
            return Response({"error": "Hostel not found"}, status=status.HTTP_404_NOT_FOUND)

        user_id = request.data.get('user_id')
        if not user_id:
            return Response({"error": "User ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        hostel.user = user
        hostel.save()

        serializer = HostelSerializer(hostel)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class UserWithoutHostelView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        # Query users without a hostel
        users_without_hostel = User.objects.exclude(hostel__isnull=False)

        # Serialize users if needed
        # Example of simple serialization (optional)
        user_list = list(users_without_hostel.values('id', 'username', 'email'))

        return Response(user_list, status=status.HTTP_200_OK)
