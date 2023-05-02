from django.db import models
from django.contrib.auth import get_user_model

from apps.category.models import Category

User = get_user_model()


class Post(models.Model):
    title = models.CharField(
        max_length=256,
        unique=True
    )
    description = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    owner = models.ForeignKey(
        User,
        related_name="posts",
        on_delete=models.SET_NULL,
        null=True
    )

    categories = models.ManyToManyField(
        Category,
        related_name="post_categories",
    )

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title
