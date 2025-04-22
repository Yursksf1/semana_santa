from django.db import models

# Create your models here.
class Video(models.Model):
    name = models.CharField(
        max_length=500,
        verbose_name="Nombre Video"
    )
    description = models.TextField(
        verbose_name="Descripcion Video"
    )

    def __str__(self):
        return self.name