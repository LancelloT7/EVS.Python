from django.db import models
import hashlib
from django.db import models
from django.utils.translation import gettext_lazy as _

class Usuario(models.Model):
    
    login = models.CharField(max_length=150, unique=True)
    senha = models.CharField(max_length=128)  # Tamanho suficiente para senhas criptografadas

    def __str__(self):
        return self.login

    
