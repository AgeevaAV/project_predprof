from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import User

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput,
        help_text="Минимум 8 символов"
    )
    password2 = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput
    )
    
    class Meta:
        model = User
        fields = ['email', 'name', 'password1', 'password2']
        labels = {
            'email': 'Email',
            'name': 'Ваше имя',
        }

