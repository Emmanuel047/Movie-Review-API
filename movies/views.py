from django.shortcuts import render
from rest_framework import viewsets
from .models import Reviews, Profile
from .serializers import ProfileSerializer, ReviewSerializer
from rest_framework.permissions import IsAuthenticated, BasePermission

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