from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Book(models.Model):
    Book_status = [
        ('available', 'available'),
        ('rented', 'rented'),
        ('sold', 'sold'),
    ]
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='covers/', null=True, blank=True)
    auther_photo = models.ImageField(upload_to='authors/', null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    rental_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    rental_period = models.IntegerField(null=True, blank=True)
    total_rental = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    availble = models.BooleanField(default=True)
    status = models.CharField(max_length=30, choices=Book_status, default='available', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.title
    
    
    
    