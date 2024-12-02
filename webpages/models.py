from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Application(models.Model):
    application = models.FileField(upload_to="media")
    application_name = models.CharField(max_length=255)
    application_text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    applicationOwner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.application_name}"
    