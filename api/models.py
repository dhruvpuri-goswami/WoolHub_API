from django.db import models

class RawWoolData(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    breed = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    micron = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
