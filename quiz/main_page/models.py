from django.core.validators import MinLengthValidator
from django.db import models

from quiz.main_page.validators import validate_file_size


class User(models.Model):
    username = models.CharField(
        max_length=30,
        unique=True,
        validators=[MinLengthValidator(6), ],
        null=False,
    )
    password = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        default='somepass'
    )
    email = models.EmailField(
        max_length=50,
        unique=True,
        null=False,
        blank=False,
    )
    profile_image = models.ImageField(
        validators=(validate_file_size,)

    )

