import random

from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    class Meta:
        indexes = [
            models.Index(fields=["created_at"]),
            models.Index(fields=["views"]),
            models.Index(fields=["likes"]),
        ]

    def __str__(self) -> str:
        return self.title

    @classmethod
    def create_dummy_data(cls, num=10):
        """
        Create dummy data for testing.
        """
        for i in range(num):
            cls.objects.create(
                title=f"Article {i}",
                content=f"This is the content of article {i}.",
                views=random.randint(0, 100_000),
                likes=random.randint(0, 1000),
            )
