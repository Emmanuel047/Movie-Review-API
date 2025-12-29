from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Reviews(models.Model):
    movie_title = models.CharField(max_length=200)
    tmdb_id = models.CharField(max_length=20, blank=True, null=True)
    poster_path = models.URLField(blank=True, null=True)
    overview = models.TextField(blank=True)
    release_date = models.DateField(blank=True, null=True)
    tmdb_rating = models.FloatField(blank=True, null=True)

    #content=review
    content = models.TextField(max_length=2000)  # Your main review text
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.movie_title} - {self.user.username}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=500, blank=True)
    favorite = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

# Auto-create Profile when User created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)