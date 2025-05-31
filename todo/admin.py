from django.contrib import admin

# Register your models here.
from .models import Task
from django.contrib import admin

admin.site.register(Task)
