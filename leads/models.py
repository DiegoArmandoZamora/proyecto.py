from django.db import models

class Lead(models.Model):
    # Estados del lead
    ESTADOS = [
        ('nuevo', 'Nuevo'),
        ('recibido', 'Recibido'),
        ('en_revision', 'En Revisión'),
        ('cotizado', 'Cotizado'),
        ('aceptado', 'Aceptado'),
        ('rechazado', 'Rechazado'),
    ]

    # Campos
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    direccion = models.TextField()
    telefono_alternativo = models.CharField(max_length=20, blank=True, null=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='nuevo')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    mensaje = models.TextField(blank=True, null=True) 
    imagen = models.ImageField(upload_to='leads/', blank=True, null=True)
    fecha_asignacion = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.telefono}"


