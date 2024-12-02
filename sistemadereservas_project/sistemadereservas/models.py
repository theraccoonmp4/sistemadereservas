from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Adicionando novos campos para o usuário

    cargo = models.CharField(max_length=100, null=True, blank=True)
    setor = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.username
