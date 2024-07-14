from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from hostel.models import Hostel
from .serializers import HostelSerializer, HostelDetailSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, permissions
from rest_framework.response import Response

class HostelCreateView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = HostelSerializer

    def post(self, request):
        user = request.user
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            hostel, created = Hostel.objects.update_or_create(
                user=user,
                defaults=serializer.validated_data
            )
            user.has_hostel = True
            user.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
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
        hostels = Hostel.objects.all()
        serializer = self.serializer_class(hostels, many=True)
        return Response(serializer.data)
    
class HostelDetailByUserView(APIView):
    serializer_class = HostelSerializer

    def get(self, request, user_id):
        try:
            hostel = Hostel.objects.get(user__id=user_id)
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
