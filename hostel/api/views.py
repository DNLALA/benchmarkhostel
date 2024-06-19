from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from hostel.models import Hostel
from .serializers import HostelSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

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
