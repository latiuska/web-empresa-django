from django.db import models

# Create your models here.


class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    subtitle = models.CharField(max_length=200, verbose_name='Subtítuo')
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(verbose_name='Imagen', upload_to="services")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación') #auto_add_now Se actualiza solo al crearlo#
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización') #auto_now se actualiza siempre que haya un cambio#
    

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ["-created"] #Con esto ordenamos. Al ponerle el - ordena de más nuevo a más viejo#

    def __str__(self):
        return self.title
