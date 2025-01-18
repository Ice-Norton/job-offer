from django.db import models

from jobs.models import JobPost
from user.models import User


# Create your models here.
class Application(models.Model):
    job = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    candidate = models.ForeignKey(User, on_delete=models.CASCADE)
    applied_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    preview = models.TextField(blank=True)



class ApplicationStatus(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    changed_at = models.DateTimeField(auto_now_add=True)
    comments = models.TextField(blank=True)