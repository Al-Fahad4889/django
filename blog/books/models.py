from django.db import models 
 
# Create your models here. 
 
class Author(models.Model): 
    name = models.CharField(max_length=100) 
    birthdate = models.DateField(null=True, blank=True) 
  
    
class Publisher(models.Model): 
    name = models.CharField(max_length=100) 
     
 
class Book(models.Model): 
    title = models.CharField(max_length=100) 
    description = models.TextField(null=True, blank=True) 
    publication_date = models.DateField(null=True, blank=True) 
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2) 
    author = models.ForeignKey(Author, on_delete=models.CASCADE,null=True, blank=True) 
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True, blank=True, related_name='books')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True,blank=True)