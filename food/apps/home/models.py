from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth.models import User

class Comment(models.Model):
    recipe_id = models.IntegerField()
    person = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commenter')
    subject = models.CharField(max_length=255)
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def serialize(self):
        return {
            "post_id": self.id,
            "recipe_id": self.recipe_id,
            "person": self.person,
            "subject": self.subject,
            "comment": self.comment,
            "timestamp": self.timestamp,
        }

class Subscribe(models.Model):
    email = models.EmailField()
    subscribed = models.BooleanField(default=False)
    person = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriber')

class Favorite(models.Model):
    recipe_id = models.IntegerField()
    favorited = models.BooleanField(default=False)
    person = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favoriter')

    def serialize(self):
        return {
            "recipe": self.recipe_id,
            "favorite": self.favorited
        }