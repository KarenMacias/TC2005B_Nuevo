from django.db import models

# Create your models here.
class User(models.Model):
    id = models.IntegerField(primary_key = True)
    names = models.CharField(max_length=60)
    lastname1 = models.CharField(max_length=30)
    lastname2 = models.CharField(max_length=30)
    created_at = models.DateTimeField()
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=30)
    username = models.CharField(max_length=20)
    birthdate = models.DateField()
    sex = models.IntegerField()
