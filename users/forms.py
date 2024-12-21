from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordResetForm, SetPasswordForm

from users.models import SyscallUser


class SyscallUserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(attrs={
            'placeholder': 'Логин',
            'required': 'required',
            'autofocus': 'autofocus'
        })
    )

    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Пароль',
            'required': 'required',
        })
    )

    class Meta:
        model = SyscallUser
        fields = ('username', 'password')


class SyscallUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(attrs={
            'placeholder': 'Логин',
            'required': 'required',
            'autofocus': 'autofocus',
        })
    )

    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Пароль',
            'required': 'required',
        })
    )

    password2 = forms.CharField(
        label='Пароль (подтверждение)',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Пароль',
            'required': 'required',
        })
    )

    email = forms.EmailField(
        label='Электронная почта',
        widget=forms.EmailInput(attrs={
            'placeholder': 'Электронная почта',
            'required': 'required',
        })
    )

    class Meta:
        model = SyscallUser
        fields = ('username', 'password1', 'password2', 'email')


class SyscallUserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label='Адрес электронной почты',
        widget=forms.EmailInput(attrs={
            'placeholder': 'Ваш email',
            'required': 'required'
        })
    )


class SyscallUserSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='Новый пароль',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Новый пароль',
            'required': 'required',
            'autofocus': 'autofocus'
        })
    )

    new_password2 = forms.CharField(
        label='Новый пароль (подтверждение)',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Подтвердите новый пароль',
            'required': 'required'
        })
    )