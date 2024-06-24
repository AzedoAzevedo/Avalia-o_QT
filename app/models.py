from django.db import models

class Usuario(models.Model):
    usuario = models.TextField(max_length=100)
    email = models.TextField(max_length=200)
    senha = models.TextField(max_length=200)

    class Meta:
        verbose_name_plural = "Usuario"

    def __str__(self):
        return f"Usuario: {self.usuario}, Email: {self.email}, Senha: {self.senha}"
