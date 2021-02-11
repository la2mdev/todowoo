from django import forms
from django.contrib.auth import authenticate
from .models import CustomUser


class SignUpForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'placeholder': 'email'}))
    username = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'username'}
    ))
    first_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'first name'}
    ))
    last_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'last name'}
    ))
    password = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'password'}
    ))
    confirmation = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'password confirmation'}
    ))

    def clean_email(self, *args, **kwargs):
        data = self.cleaned_data
        email = data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            self.add_error('email', 'Username ya en uso en la plataforma')
        return email

    def clean_username(self, *args, **kwargs):
        data = self.cleaned_data
        username = data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            self.add_error('username', 'Nombre ya en uso en la plataforma')
        return username

    def clean(self, *args, **kwargs):
        data = super(SignUpForm, self).clean(*args, **kwargs)
        password = data.get('password')
        confirmation = data.get('confirmation')
        if password != confirmation:
            self.add_error('confirmation', 'Passwords no coinciden')
        return data

    def save(self, *args, **kwargs):
        data = self.cleaned_data
        email = data.get('email')
        username = data.get('username')
        first_name = date.get('first_name')
        last_name = data.get('last_name')
        password = data.get('password')
        user = CustomUser.objects.create_user(
            email=email, username=username, first_name=first_name,
            last_name=last_name, password=password)
        return User


class LoginForm(forms.Form):
    email = forms.CharField(required=True, widget=forms.EmailInput(
        attrs={'placeholder': 'email'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'password'}))

    def clean(self, *args, **kwargs):
        data = super(LoginForm, self).clean(*args, **kwargs)
        email = data.get('email')
        password = data.get('password')
        user = authenticate(email=email, password=password)
        if user is None:
            raise forms.ValidationError('Usuario o contraseña incorrectas')
        return data

    def save(self, *args, **kwargs):
        data = self.cleaned_data
        email = data.get('email')
        password = data.get('password')
        user = authenticate(email=email, password=password)
        return user
