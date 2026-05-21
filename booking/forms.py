from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Booking


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Логин', min_length=6)
    full_name = forms.CharField(label='ФИО')
    phone = forms.CharField(label='Телефон')
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput, min_length=8)
    password2 = forms.CharField(label='Подтверждение', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'full_name', 'phone', 'email', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 6:
            raise forms.ValidationError('Логин минимум 6 символов')
        if not username.isalnum():
            raise forms.ValidationError('Только буквы и цифры')
        return username


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room', 'date', 'payment']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }