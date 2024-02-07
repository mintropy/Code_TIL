import uuid

from django.db import models

from config.models import BaseModel


class Community(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
