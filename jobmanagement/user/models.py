from django.contrib.auth.models import AbstractUser
from django.db import models

from jobs.models import Skill


class User(AbstractUser):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)


class CandidateProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill)
    education = models.TextField()
    experience = models.TextField()
    resume = models.FileField(
        upload_to='',
        validators=[],
        blank=True
    )




