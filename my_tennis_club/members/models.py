from django.db import models
from django.utils import timezone

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True, blank=True, default=None)  # ✅ allows empty value

    def __str__(self):
        return f"{self.firstname} {self.lastname}"