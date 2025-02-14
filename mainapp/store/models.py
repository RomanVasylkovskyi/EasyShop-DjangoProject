from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Publisher(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Section(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", null=True, blank=True)
    author = models.CharField(max_length=255)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name="products")
    language = models.CharField(max_length=50)
    cover_type = models.CharField(max_length=50)
    pages = models.PositiveIntegerField()
    format = models.CharField(max_length=20)
    illustrations = models.CharField(max_length=50)
    year_published = models.PositiveIntegerField()
    isbn = models.CharField(max_length=20, unique=True)
    weight = models.PositiveIntegerField(help_text="Вага (в грамах)")
    sections = models.ManyToManyField(Section, related_name="products", blank=True)

    def __str__(self):
        return self.name

class ProductAdmin(models.Model):
    is_featured = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Admin settings for {self.product.name}"
