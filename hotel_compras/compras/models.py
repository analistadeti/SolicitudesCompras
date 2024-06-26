from django.db import models
from django.contrib.auth.models import User

class SolicitudCompra(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    solicitante = models.ForeignKey(User, on_delete=models.CASCADE)
    descripcion = models.TextField()
    estado = models.CharField(max_length=100, default='Solicitado')
    departamento = models.ForeignKey('Departamento', on_delete=models.SET_NULL, null=True, blank=True)  # Nuevo campo

    def __str__(self):
        return f'Solicitud de compra #{self.id}'

class EstadoCompra(models.Model):
    estado = models.CharField(max_length=100)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    actualizado_por = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.estado

class Departamento(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.username

