from django import forms
from .models import Book, Category

class Book_form(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'cover',
            'auther_photo',
            'pages',
            'price',
            'rental_price',
            'rental_period',
            'total_rental',
            'status',
            'category',
            ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'cover': forms.FileInput(attrs={'class': 'form-control'}),
            'auther_photo': forms.FileInput(attrs={'class': 'form-control'}),
            'pages': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'rental_price': forms.NumberInput(attrs={'class': 'form-control', 'id':'rentalprice'}),
            'rental_period': forms.NumberInput(attrs={'class': 'form-control', 'id':'rentalperiod'}),
            'total_rental': forms.NumberInput(attrs={'class': 'form-control', 'id':'totalrental'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            }
        
class Category_form(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),   
            }