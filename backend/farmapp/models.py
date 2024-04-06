from typing import Any
from django.db import models
from django.contrib.auth.models import User, AbstractUser, BaseUserManager
#import uuid

# class Farm(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     ime = models.CharField("Ime", max_length=30)
#     prezime = models.CharField("Prezime", max_length=30)
#     naziv_opg = models.CharField("Naziv OPG-a", max_length=100)
#     adresa = models.CharField(max_length=255)
#     telefon = models.IntegerField("Telefon")
#     email = models.EmailField()

#     def __str__(self):
#         return f"{self.ime} {self.prezime} - {self.naziv_opg}"

# class Product(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     CATEGORY_CHOICES = [
#         ('milk_product', 'Mliječni proizvodi'),
#         ('fruit_product', 'Voće'),
#         ('vegetables_product', 'Povrće'),
#     ]
    
#     farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
#     detail = models.TextField()

#     def __str__(self):
#         return f"{self.name.capitalize()} ({self.category.capitalize()})"

##################################################################################################


class UserManager(BaseUserManager):
    def create_user(self, ime: str, prezime: str, naziv_opg: str, adresa: str, telefon: str, email: str, password: str = None, is_staff=False, is_superuser=False):# -> "User":  
        if not ime:
            raise ValueError('User must have an ime!')
        if not prezime:
            raise ValueError('User must have an prezime!')
        if not naziv_opg:
            raise ValueError('User must have an naziv_opg!')
        if not adresa:
            raise ValueError('User must have an adresa!')
        if not telefon:
            raise ValueError('User must have an telefon!')
        if not email:
            raise ValueError('User must have an email!')
        if not password:
            raise ValueError('User must have an password!')
        
        user = self.model(email=self.normalize_email(email))
        user.ime = ime
        user.prezime = prezime
        user.naziv_opg = naziv_opg
        user.adresa = adresa
        user.telefon = telefon
        user.email = email
        user.set_password(password)
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()
        
        return user
    
    def create_superuser(self, ime: str, prezime: str, naziv_opg: str, adresa: str, telefon: str, email: str, password: str = None): # -> "User":
        user = self.create_user(ime=ime, prezime=prezime, naziv_opg=naziv_opg, adresa=adresa, telefon=telefon, email=email, password=password, is_staff=True, is_superuser=True)
        user.save()
        
        return user

class Farm(AbstractUser):
    ime = models.CharField("Ime", max_length=150)
    prezime = models.CharField("Prezime", max_length=150)
    naziv_opg = models.CharField("Naziv OPG-a", max_length=150)
    adresa = models.CharField(max_length=255)  
    telefon = models.BigIntegerField("Telefon")
    email = models.EmailField(unique=True, max_length=150)
    password = models.CharField(max_length=150)
    username = None

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['ime', 'prezime', 'naziv_opg', 'adresa', 'telefon']
    
    
class Product(models.Model):
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