from django.db import models

from modules.models import BaseModel

# Create your models here.


class Todo(BaseModel):
    title = models.CharField(max_length=255, null=True, default=None)
    description = models.TextField(null=True, default=None)
    priority = models.IntegerField(default=0)
