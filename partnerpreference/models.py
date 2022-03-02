from msilib.schema import CheckBox
from tkinter import Widget
from django.db import models

from userprofile.models import UserProfile 

# Create your models here.

class Preference(models.Model):
    marital_status = models.CharField(max_length=100)
    