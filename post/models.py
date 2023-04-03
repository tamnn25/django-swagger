from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name="comments")
    message = models.TextField()

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post.title


@receiver(post_save, sender=Comment)
def _post_save_receiver(sender, **kwargs):
    print("receiver-comment")
