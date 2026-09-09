from django import forms

from .models import Visitor


class VisitorForm(forms.ModelForm):
    """Форма ввода имени на главной странице.

    Строится на основе модели Visitor, поэтому автоматически наследует
    её валидацию (max_length, запрет пустой/пробельной строки).
    """

    class Meta:
        model = Visitor
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Введите ваше имя",
                    "autofocus": True,
                    "autocomplete": "off",
                }
            )
        }
        labels = {"name": "Ваше имя"}
        error_messages = {
            "name": {
                "required": "Пожалуйста, введите имя — поле не может быть пустым.",
                "max_length": "Имя слишком длинное (не более 100 символов).",
            }
        }
