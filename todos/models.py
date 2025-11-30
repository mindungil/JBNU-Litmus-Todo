from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='todos_user_set',
        related_query_name='todos_user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='todos_user_set',
        related_query_name='todos_user',
    )

class Todo(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    start_at = models.DateTimeField(default=timezone.now)
    end_at = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['is_completed', 'end_at', '-created_at']

    def __str__(self):
        return self.title
    
    def clean(self):
        if self.end_at and self.end_at < self.start_at:
            raise ValidationError("마감일은 시작일보다 이후여야 합니다.")
    