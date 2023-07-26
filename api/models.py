from django.db import models


class Todo(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    pub_date = models.DateTimeField("Date published", auto_now_add=True)
    to_date = models.DateTimeField("Assigned date", null=True, blank=True)
    done = models.BooleanField(default=False)
