# forms.py
from django import forms
from django.core.validators import MinLengthValidator
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'login', 'password']
        widgets = {
            'password': forms.PasswordInput(),  # Render the password field as a password input
        }
        labels = {
            'first_name': "Ім'я",
            'last_name': "Прізвище",
            'email': "Пошта",
            'phone_number': "Номер телефону",
            'login': "Логін",
            'password': "Пароль",
        }
        help_texts = {
            'password': "Пароль повинен містити щонайменше 8 символів.",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add a MinLengthValidator to the password field
        self.fields['password'].validators.append(MinLengthValidator(8))