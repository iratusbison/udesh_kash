from django.db import models
from django.contrib.auth.models import AbstractUser

class Staff(AbstractUser):
    name = models.CharField(max_length=20)
    department = models.CharField(max_length = 100)
    salary = models.DecimalField(max_digits=10, decimal_places=2,null=True)

    
    groups = models.ManyToManyField(
        'auth.Group',
       related_name='staff_members',
       blank=True,
       help_text = 'The groups this staff member belongs to.',
       verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
       related_name = 'staff_members',
       blank=True,
       help_text = 'Specific permission for this staff member.',
       verbose_name='user permissions',

    )


    def __str__ (self):
        return self.username