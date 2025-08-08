from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import User, Profile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label=_("Email"),
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': _('example@example.com'),
            'autocomplete': 'email'
        }),
        help_text=_("Обязательное поле. Введите действующий email.")
    )

    username = forms.CharField(
        label=_("Имя пользователя"),
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('username'),
            'autocomplete': 'username'
        }),
        help_text=_("Только буквы, цифры и @/./+/-/_.")
    )

    password1 = forms.CharField(
        label=_("Пароль"),
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': _('Пароль'),
            'autocomplete': 'new-password'
        }),
        help_text=_("""
            <ul class="password-requirements">
                <li>Минимум 8 символов</li>
                <li>Не должен быть похож на имя пользователя</li>
                <li>Не должен быть слишком простым</li>
            </ul>
        """)
    )

    password2 = forms.CharField(
        label=_("Подтверждение пароля"),
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': _('Подтвердите пароль'),
            'autocomplete': 'new-password'
        }),
        help_text=_("Введите тот же пароль, что и выше, для проверки.")
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError(
                _("Пользователь с таким email уже существует."))
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError(_("Это имя пользователя уже занято."))
        return username


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")
        labels = {
            'username': 'Имя пользователя',
            'email': 'Email',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password', None)


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("birthday", "image")
        labels = {
            'birthday': 'Дата рождения',
            'image': 'Аватар',
        }
        widgets = {
            'birthday': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                },
                format='%Y-%m-%d'
            ),
        }
