from django.shortcuts import render
from rest_framework import viewsets
from .models import Reviews, Profile
from .serializers import ProfileSerializer, ReviewSerializer

# Create your views here.
class ProfileSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ReviewSet(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer