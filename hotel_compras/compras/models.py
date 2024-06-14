from django.db import models
from django.contrib.auth.models import User

class SolicitudCompra(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    solicitante = models.ForeignKey(User, on_delete=models.CASCADE)
    descripcion = models.TextField()
    estado = models.CharField(max_length=100, default='Solicitado')

    def __str__(self):
        return f'Solicitud de compra #{self.id}'

class EstadoCompra(models.Model):
    solicitud = models.ForeignKey(SolicitudCompra, on_delete=models.CASCADE)
    estado = models.CharField(max_length=100)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    actualizado_por = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.estado} - {self.solicitud}'

# Create your models here.
