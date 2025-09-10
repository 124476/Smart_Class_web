from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from apps.users.models import User, Profile, RegistrationToken


class SignUpForm(UserCreationForm):
    registration_token = forms.CharField(
        label='Регистрационный токен',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Токен',
            'autocomplete': 'email'
        }),
        help_text='Введите токен, полученный от администратора'
    )
    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'example@example.com',
            'autocomplete': 'email'
        }),
        help_text="Обязательное поле. Введите действующий email."
    )

    username = forms.CharField(
        label="Имя пользователя",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'username',
            'autocomplete': 'username'
        }),
        help_text="Только буквы, цифры и @/./+/-/_."
    )

    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Пароль',
            'autocomplete': 'new-password'
        }),
        help_text="""
            <ul class="password-requirements">
                <li>Минимум 8 символов</li>
                <li>Не должен быть похож на имя пользователя</li>
                <li>Не должен быть слишком простым</li>
            </ul>
        """
    )

    password2 = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Подтвердите пароль',
            'autocomplete': 'new-password'
        }),
        help_text="Введите тот же пароль, что и выше, для проверки."
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError(
                "Пользователь с таким email уже существует.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("Это имя пользователя уже занято.")
        return username

    def clean_registration_token(self):
        token_value = self.cleaned_data.get('registration_token')
        try:
            token = RegistrationToken.objects.get(token=token_value)
        except RegistrationToken.DoesNotExist:
            raise ValidationError('Неверный регистрационный токен')

        if not token or not token.is_active:
            raise ValidationError('Токен уже использован или истек')

        return token_value


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
