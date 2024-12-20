from django.db import models
from django.contrib.auth.models import User
from webpages.models import Company

# Create your models here.
class ClientViewPermission(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    company_profile = models.ForeignKey(Company, on_delete=models.CASCADE)
    allow = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.client.email} - {self.company_profile.company_name}, {self.allow}"