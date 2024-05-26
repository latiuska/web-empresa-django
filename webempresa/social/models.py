from django.db import models

# Create your models here.

class Link(models.Model):
    key = models.SlugField(verbose_name='nombre clave', max_length=100, unique=True)
    name =models.CharField(verbose_name="Red social", max_length=200)
    url =models.URLField(verbose_name="Enlace", max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación') #auto_add_now Se actualiza solo al crearlo#
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización') #auto_now se actualiza siempre que haya un cambio#
    

    class Meta:
        verbose_name = "Enlace"
        verbose_name_plural = "Enlaces"
        ordering = ["-name"] #Con esto ordenamos. Al ponerle el - ordena de más nuevo a más viejo#

    def __str__(self):
        return self.name
