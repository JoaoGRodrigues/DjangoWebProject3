from django.db import models
from django.utils import timezone
from datetime import datetime


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    text = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

from django.db import models

class Invite(models.Model):
    name = models.CharField(max_length=500)
    branch = models.CharField(max_length=500)
    GENDER_CHOICES = (
      ("M", "Male"),
      ("F", "Female"),
      ("O", "Other"),
      ("?", "Unknown")
    )
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default="?"
    )
    date_of_birth = models.DateField(null=True, blank=True)
    RACE_CHOICES = (
        ("ASIAN", "Asian"),
        ("BLACK", "Black"),
        ("LATINO", "Latino"),
        ("WHITE", "White"),
        ("OTHER", "Other"),
        ("?", "Unknown"),
    )
    race = models.CharField(
        max_length=10,
        choices=RACE_CHOICES,
        default="?"
    )
    notes = models.TextField(blank=True)

# Create your models here.
class AMOS(models.Model):
    dataSource = models.CharField(max_length=500, default='Nome da fonte de dados')
    SimNao = (
        ("Y", "Yes"),
        ("N", "No"),
        ("DN", "Dont know")
    )
    has_errors= models.CharField(
        max_length=2,
        choices=SimNao,
        default="DN"
    )
    exec_start = models.DateTimeField(default=timezone.now)
    exec_end =  models.DateTimeField(default=timezone.now)
    erros_prep = models.CharField(max_length=5000, default=' ')
    erros_executing = models.CharField(max_length=5000, default=' ')
    erros_saving = models.CharField(max_length=5000, default=' ')
    notes = models.TextField(blank=True)
    def publish(self):
            self.published_date = timezone.now()
            self.save()
