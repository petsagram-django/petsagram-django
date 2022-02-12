from datetime import datetime

from django.core.validators import MinLengthValidator
from django.db import models

from petsatgram.main.validators import validate_letters, validate_file_size


class Profile(models.Model):
    # good practice is to use class vars
    FIRST_NAME_MAX_LENGTH = 30
    FIRST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2
    # for choices
    GENDER_TYPE = ['Male', 'Female', 'Do not show']

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            # build in validator
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            # created validator, look in validators.py
            validate_letters
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validate_letters
        )
    )

    picture_url = models.URLField(
        verbose_name="Link to profile picture",
    )

    date_of_birth = models.DateField(
        # add if you want django administration with blank fields
        null=True,
        blank=True,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    email = models.EmailField(
        null=True,
        blank=True,
    )

    gender = models.CharField(
        max_length=max(len(x) for x in GENDER_TYPE),
        choices=((x, x) for x in GENDER_TYPE),
        null=True,
        blank=True,
    )

    def __str__(self):
        # goood practice is to have str method for presentation
        return f'{self.first_name} {self.last_name}'


class Pet(models.Model):
    PET_NAME_MAX_LENGTH = 30
    TYPES = ["Cat", "Dog", "Bunny", "Parrot", "Fish", "Other"]

    name = models.CharField(
        max_length=PET_NAME_MAX_LENGTH,
    )

    type = models.CharField(
        max_length=max(len(x) for x in TYPES),
        choices=((x, x) for x in TYPES)
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,

    )
    # one to many relation
    user_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )

    @property
    def age(self):
        # calculate age
        return datetime.now().year - self.date_of_birth.year

    def __str__(self):
        return f'{self.name}'

    class Meta:
        # unique name for unique user, not unique name in the db
        unique_together = ('user_profile', 'name')


class PetPhoto(models.Model):
    # photo = models.FileField(
    #     upload_to='files/',
    #     verbose_name="",
    #     validators=[validate_file_size]
    # )

    photo = models.ImageField(
        upload_to='media/',
        verbose_name="",
        validators=[validate_file_size]
    )

    # many to many relation
    tagged_pets = models.ManyToManyField(
        to=Pet,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )
    # auto_now for update
    created_on = models.DateTimeField(
        auto_now_add=True,

    )

    likes = models.IntegerField(
        default=0,
    )

    # one to many again, don't forget on_delete
    user_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )
