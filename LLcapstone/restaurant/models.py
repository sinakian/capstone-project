from django.db import models

# Create your models here.
class booking(models.Model):
    name=models.CharField(max_length=255)
    no_of_guests=models.IntegerField()
    bookingdate=models.DateTimeField()
    
class menu(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    inventory = models.IntegerField()
   