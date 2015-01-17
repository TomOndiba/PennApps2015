from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    EUNUCH = 'E'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (EUNUCH, 'Eunuch'),
    )

    UNKNOWN = 'UN'
    SINGLE = 'SI'
    RELATIONSHIP = 'RE'
    ENGAGED = 'EN'
    MARRIED = 'MA'
    CIVIL_UNION = 'CI'
    DOMESTIC_PARTNERSHIP = 'DO'
    OPEN_RELATIONSHIP = 'OP'
    COMPLICATED = 'CO'
    SEPARATED = 'SE'
    DIVORCED = 'DI'
    WIDOWED = 'WI'

    RELATIONSHIP_CHOICES = (
        (UNKNOWN, 'Unknown'),
        (SINGLE, 'Single'),
        (RELATIONSHIP, 'In a relationship'),
        (ENGAGED, 'Engaged'),
        (MARRIED, 'Married'),
        (CIVIL_UNION, 'In a civil union'),
        (DOMESTIC_PARTNERSHIP, 'In a domestic partnership'),
        (OPEN_RELATIONSHIP, 'In an open relationship'),
        (COMPLICATED, "It's complicated"),
        (SEPARATED, 'Separated'),
        (DIVORCED, 'Divorced'),
        (WIDOWED, 'Widowed'),
    )

    user = models.OneToOneField(User)
    age = models.IntegerField(null=True)
    location = models.CharField(max_length=255, blank=True)
    gender = models.CharField(max_length=1,
                              choices=GENDER_CHOICES,
                              default=EUNUCH)
    email = models.EmailField(blank=True)
    relationship_status = models.CharField(max_length=2,
                                           choices=RELATIONSHIP_CHOICES,
                                           default=UNKNOWN)

