from django.contrib import admin
from .models import CustomUser
from django.contrib.admin import ModelAdmin
# Register your models here.

admin.site.register(CustomUser,ModelAdmin)