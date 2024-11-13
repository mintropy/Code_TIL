from django.db import models

from modules.models import BaseModel


class Community(BaseModel):
    posts: models.QuerySet["Post"]
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title


class Post(BaseModel):
    community = models.ForeignKey(
        Community, on_delete=models.SET_NULL, null=True, related_name="posts"
    )
    post_no = models.IntegerField(default=None, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    likes = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-created_at"]
        constraints = [
            models.UniqueConstraint(
                fields=["community", "post_no"],
                name="unique_community_post_no",
                condition=models.Q(community__isnull=False),
            )
        ]


class PopularPost(Post):
    class Meta:
        proxy = True
        ordering = ["-likes", "-created_at"]


class AdminPost(Post):
    fixed = models.BooleanField(default=False)


class Reply(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="replies")
    content = models.TextField()
    likes = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.post.title} - {self.content[:20]}"
