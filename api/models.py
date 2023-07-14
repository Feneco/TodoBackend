from django.db import models
import string
import random


# Create your models here.
class Project(models.Model):
    name        = models.CharField(max_length=256)
    description = models.CharField(max_length=256)


class Todo(models.Model):
    name        = models.CharField    (max_length=256                                )
    description = models.CharField    (max_length=256                                )
    pub_date    = models.DateTimeField("Date published", auto_now_add=True           )
    to_date     = models.DateTimeField("Assigned date",                   null=True, blank=True )
    project     = models.ForeignKey   (Project, on_delete=models.CASCADE, null=True, blank=True )
    blocking    = models.ForeignKey   ("self", on_delete=models.CASCADE,  null=True, blank=True )
    done        = models.BooleanField (default=False)
