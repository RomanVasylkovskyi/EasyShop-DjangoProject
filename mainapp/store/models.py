from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # ForeignKey для категорії

    def __str__(self):
        return self.name


class ProductAdmin(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    is_featured = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Admin settings for {self.product.name}"
