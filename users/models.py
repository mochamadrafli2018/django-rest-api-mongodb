from django.db import models
import uuid
# importing validationerror
from django.core.exceptions import ValidationError
 
# email validator function
def validate_email(value):
    if "@" in value:
        return value
    else:
        raise ValidationError("Enter correct email")

# password validator function
def validate_password(value):
    if len(value) > 8:
        return value
    else:
        raise ValidationError("Password must be equal or more than 8 characters")

# Create your models here.
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, blank=False, default='')
    email = models.EmailField(unique=True, blank=False, validators =[validate_email],
                              error_messages={
                                  'unique': "A user with that email already exists.",
                              })
    password = models.CharField(max_length=20, blank=False, default='', validators =[validate_password])

    # enum data type
    class UserGender(models.TextChoices):
        MALE = 'male'
        FEMALE = 'female'
    gender = models.CharField(max_length=6, choices=UserGender.choices, default=UserGender.MALE) 

    # enum data type
    class UserRole(models.TextChoices):
        ADMIN = 'admin'
        MEMBER = 'member'
    role = models.CharField(max_length=6, choices=UserRole.choices, default=UserRole.ADMIN)
    # boolean data
    is_active = models.BooleanField(default=True)