from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Videojuego(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField()
    category = models.ForeignKey(
        Category, related_name="videojuegos", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

# Create your models here.
