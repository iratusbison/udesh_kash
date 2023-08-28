from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin','Admin'),
        ('manager','Manager'),
        ('employee','Employee'),
    ) 
    role = models.CharField(max_length=10, choices=ROLE_CHOICES,default='employee')

    def __str__(self):
        return self.username
    
    class Meta:
        permissions = [
            ('view_resource', 'Can view resource'),
            ('change_resource', 'Can change resource'),
            ('add_resource', 'Can add resource'),
            ('delete_resource', 'Can delete resource'),
        ]
