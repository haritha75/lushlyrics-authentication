from django.db import models

class CustomUser(models.Model):
    # Additional fields
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
