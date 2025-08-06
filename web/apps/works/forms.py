from django import forms
from apps.works.models import Event, Feedback


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["title", "description", "date"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите название события",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Опишите событие",
                    "rows": 4,
                }
            ),
            "date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        }
        labels = {
            "title": "Название события",
            "description": "Описание",
            "date": "Дата проведения",
        }


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["message"]
        widgets = {
            "message": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Напишите ваш отзыв или пожелание...",
                    "rows": 5,
                }
            ),
        }
        labels = {
            "message": "Сообщение",
        }
