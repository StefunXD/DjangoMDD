from django.contrib import admin

# Register your models here.
from .models import Questions, Answers

admin.site.register(Questions)
admin.site.register(Answers)