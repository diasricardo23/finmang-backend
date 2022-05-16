from email.policy import default
from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    properties = models.JSONField(default=dict, blank=True, null=True)

    class Meta:
        ordering = ['created_at']