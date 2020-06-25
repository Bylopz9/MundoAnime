from django.db import models

# Create your models here.

class Servicios(models.Model):
    titulo=models.CharField(max_length=50, verbose_name="Servicio")
    contenido=models.CharField(max_length=50,verbose_name="Descripción")
    imagen=models.ImageField()
    created=models.DateTimeField(auto_now=True,verbose_name="Creación")
    update=models.DateTimeField(auto_now=True,verbose_name="Actualización")

    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'
    
    def __str__(self):
        return self.titulo
