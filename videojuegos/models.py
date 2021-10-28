from django.db import models


class Videojuego(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField()
    

    def __str__(self):
        return self.name

# Create your models here.
