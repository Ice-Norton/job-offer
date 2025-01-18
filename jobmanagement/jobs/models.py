from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class JobPost(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField()
    experience_required = models.IntegerField(default=0)
    status = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    salary_range = models.CharField(max_length=100, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    pic_post = models.ImageField(upload_to=(""), null=True)
    employment_type = models.CharField(max_length=100)


class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)