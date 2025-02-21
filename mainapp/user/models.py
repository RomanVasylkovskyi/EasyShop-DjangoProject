from django.db import models
from django.core.validators import MinLengthValidator


class User(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Ім'я")
    last_name = models.CharField(max_length=100, verbose_name="Прізвище")
    email = models.EmailField(unique=True, verbose_name="Пошта")
    phone_number = models.CharField(max_length=15, unique=True, verbose_name="Номер телефону")
    login = models.CharField(max_length=100, verbose_name="Логін")
    password = models.CharField(max_length=256, validators=[MinLengthValidator(8)], verbose_name="Пароль")

    def __str__(self):
        return f"{self.login} {self.first_name}  {self.last_name}  {self.phone_number}"


class Admin(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ім'я")
    password = models.CharField(max_length=256, validators=[MinLengthValidator(8)], verbose_name="Пароль")

    def __str__(self):
        return f"{self.name}"


class Meta:
    verbose_name = "Адміністратор"
    verbose_name_plural = "Адміністратори"
