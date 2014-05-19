from django.db import models
from app_main.models import ClassPl, ClassPg


class ClassB(ClassPl):
    title = models.CharField(max_length=255)


class ClassA(models.Model):
    title = models.CharField(max_length=255)
    page = models.ForeignKey(ClassPg)
