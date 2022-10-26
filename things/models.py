from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.core.validators import RegexValidator


class Thing(models.Model):
    name = models.CharField(max_length=35, unique=True)
    description = models.CharField(max_length=120, blank=True)
    quantity = models.IntegerField(
        validators=[MinValueValidator(0),MaxValueValidator(50)]
    )
    created_at = models.DateTimeField(auto_now_add=True)



class User(AbstractUser):
    username = models.CharField(
    max_length=30,
    unique=True,
    validators=[RegexValidator(
        regex=r'^@\w{3,}$',
        message='Username must consist of @ symbol followed by at least 3 alphanumericals'
        )]
    )

    first_name = models.CharField(
    max_length=50,
    blank=False,
    null=False,
    unique=False
    )

    last_name = models.CharField(
    max_length=50,
    blank=False,
    null=False,
    unique=False
    )

    email = models.EmailField(
    unique=True,
    blank=False
    )

    bio = models.CharField(
    max_length=520,
    blank=True
    )



class Post(models.Model):
    """Posts by users in their microblogs."""

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Model options."""

        ordering = ['-created_at']
