from django.db import models
from django.contrib.auth.models import User


# Create your models here.

#Model for user Profile Information
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    firstName = models.CharField(max_length=100, null=True)
    lastName = models.CharField(max_length=100, null=True)
    bio = models.TextField(null=True)
    age = models.IntegerField(null=True)
    profile_picture = models.ImageField(upload_to='static/images', null=True, blank=True)
    

    def __str__(self):
        return str(self.user)
    

class Characters(models.Model):
    CHARACTER_CHOICES = (
        ('W', 'Whale'),
        ('D', 'Dolphin'),
        ('T', 'Turtle'),
        ('S', 'Seal'),
        ('G', 'Seagull'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    character = models.CharField(max_length=1, choices=CHARACTER_CHOICES)
    character_picture = models.ImageField(upload_to='static/images', null=True, blank=True)


    def __str__(self):
        return f'{self.user} - {self.get_character_display()}'