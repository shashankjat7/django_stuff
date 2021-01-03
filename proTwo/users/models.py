from django.db import models

# Create your models here.

class user(models.Model):
    name = models.CharField(max_length=254)
    age = models.IntegerField()
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name