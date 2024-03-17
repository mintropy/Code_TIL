from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class LikedPost(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    posts = models.JSONField()

    def like_post(self, post_id: int) -> None:
        if self.posts.get(str(post_id)):
            self.posts.pop(str(post_id))
        else:
            self.posts[str(post_id)] = True
        self.save(update_fields=["posts"])


class LikedComment(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    comments = models.JSONField()

    def like_comment(self, comment_id: int) -> None:
        if self.comments.get(str(comment_id)):
            self.comments.pop(str(comment_id))
        else:
            self.comments[str(comment_id)] = True
        self.save(update_fields=["comments"])
