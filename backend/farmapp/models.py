from django.db import models
from django.contrib.auth.models import User
import uuid

class Farm(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ime = models.CharField("Ime", max_length=30)
    prezime = models.CharField("Prezime", max_length=30)
    naziv_opg = models.CharField("Naziv OPG-a", max_length=100)
    adresa = models.CharField(max_length=255)
    telefon = models.IntegerField("Telefon")
    email = models.EmailField()

    def __str__(self):
        return f"{self.ime} {self.prezime} - {self.naziv_opg}"

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    CATEGORY_CHOICES = [
        ('milk_product', 'Mliječni proizvodi'),
        ('fruit_product', 'Voće'),
        ('vegetables_product', 'Povrće'),
    ]
    
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    detail = models.TextField()

    def __str__(self):
        return f"{self.name.capitalize()} ({self.category.capitalize()})"
