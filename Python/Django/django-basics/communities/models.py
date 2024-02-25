from django.db import models

from modules.models import BaseModel


class Community(BaseModel):
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title


class Post(BaseModel):
    community = models.ForeignKey(
        Community, on_delete=models.SET_NULL, null=True, related_name="posts"
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    likes = models.PositiveIntegerField(default=0)


class PopularPost(Post):
    class Meta:
        proxy = True
        ordering = ["-likes"]


class AdminPost(Post):
    fixed = models.BooleanField(default=False)
