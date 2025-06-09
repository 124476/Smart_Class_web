import django.forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    email = django.forms.EmailField(required=True, label='Email')
    first_name = django.forms.CharField(max_length=150, required=True, label='Имя')
    last_name = django.forms.CharField(max_length=150, required=True, label='Фамилия')
    avatar = django.forms.ImageField(required=False, label='Аватар')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'avatar')
        labels = {
            'username': 'Имя пользователя',
        }

class CustomUserChangeForm(django.forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'avatar')
        labels = {
            'username': 'Имя пользователя',
            'avatar': 'Аватар',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'password1' in self.fields:
            del self.fields['password1']
        if 'password2' in self.fields:
            del self.fields['password2']