from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models import DO_NOTHING


class Category(models.Model):
    name = models.CharField(
        max_length=30,
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Question(models.Model):
    question = models.TextField(
        max_length=300,
        validators=[MinLengthValidator(10),],
    )
    option_1 = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        default="A",
    )
    option_2 = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        default="B",
    )
    option_3 = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        default="C",
    )
    option_4 = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        default="D",
    )
    correct_option = models.CharField(
        choices=(
            ("A", "A"),
            ("B", "B"),
            ("C", "C"),
            ("D", "D"),
        ),
        default=option_4,
        max_length=200,
        blank=False,
        null=False,
    )

    topic = models.ForeignKey(
        Category,
        on_delete=models.DO_NOTHING,
        default=None,
        null=True,
        blank=True,
    )

class Quiz(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    duration = models.DurationField()
    difficulty = models.CharField(max_length=20)
    questions = models.ManyToManyField(Question)

    class Meta:
        verbose_name_plural = "Quizes"