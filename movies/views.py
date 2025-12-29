from django.shortcuts import render
from rest_framework import viewsets
from .models import Reviews, Profile
from .serializers import ProfileSerializer, ReviewSerializer
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegistrationSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True #AnyoneCan read
        return obj.profile.user == request.user #-Owner can write
class ProfileSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ReviewSet(viewsets.ModelViewSet):
    #Order is newest first
    queryset = Reviews.objects.all().order_by('-created_at')
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
     #Fields to  Search
    search_fields = ['movie_title', 'content'] 
    filterset_fields = ['rating', 'tmdb_rating']

    def get_queryset(self):  # ✅ ADD USER FILTER
        return Reviews.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

@api_view(['POST'])
@permission_classes([AllowAny])  # No auth required
def register_user(request):
    serializer = RegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'message': 'User created successfully!',
            'username': serializer.validated_data['username']
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

