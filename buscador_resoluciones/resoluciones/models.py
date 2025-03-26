from django.db import models

class Resolucion(models.Model):
    res = models.CharField(max_length=50, verbose_name="Resolución")
    cod = models.CharField(max_length=50, verbose_name="Código")
    expte = models.CharField(max_length=100, verbose_name="Expediente")
    tema = models.TextField(verbose_name="Tema")
    pdf = models.URLField(verbose_name="Enlace PDF")
    year = models.CharField(max_length=4, verbose_name="Año")

    def __str__(self):
        return f"{self.res} - {self.tema}"