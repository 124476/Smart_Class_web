from django import forms

from apps.problems.models import Status, Problem


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название статуса'
            })
        }
        labels = {
            'name': 'Название статуса'
        }


class ProblemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ProblemForm, self).__init__(*args, **kwargs)

        # Если пользователь передан, ограничиваем выбор статусов
        if user:
            self.fields['status'].queryset = Status.objects.all()

        # Настройка виджетов
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название проблемы'
        })
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Опишите проблему подробно'
        })
        self.fields['status'].widget.attrs.update({
            'class': 'form-select'
        })

    class Meta:
        model = Problem
        fields = ['name', 'status', 'description']
        labels = {
            'name': 'Название проблемы',
            'status': 'Статус',
            'description': 'Описание'
        }