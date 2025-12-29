from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Reviews
from .services import TMDBService

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    user_profile = ProfileSerializer(source='user.profile', read_only=True)
    class Meta:
        model = Reviews
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password_confirm')


    def create(self, validated_data):
        validated_data.pop('password_confirm')
        return User.objects.create_user(**validated_data)


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reviews
        fields = ['id',
                    'movie_title',
                    'content',
                    'rating',
                    'tmdb_id',
                    'poster_path',
                    'tmdb_rating',
                    'overview', 'created_at']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user

        movie_title = validated_data.get('movie_title')
        if movie_title:
            tmdb_data = TMDBService.search_movie(movie_title)
            if tmdb_data:
                validated_data['movie_title'] = movie_title
                validated_data.update(tmdb_data)

        return super().create(validated_data)