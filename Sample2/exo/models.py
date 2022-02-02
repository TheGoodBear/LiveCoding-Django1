from django.db import models

# Create your models here.

class Person(models.Model):
    """
    """
    
    name = models.CharField(
        "Nom",
        max_length=30)
    sex = models.CharField(
        "Sexe",
        max_length=1)
    
    
    def __str__(self) -> str:       
        return f"{self.name}"