from django.db import models

# Create your models here.
class Product(models.Model): 
    name = models.CharField(max_length=100) 
    description = models.TextField(null=True, blank=True) 
    publication_date = models.DateField(null=True, blank=True) 
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2) 
    