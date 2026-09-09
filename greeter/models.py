from django.core.exceptions import ValidationError
from django.db import models


def validate_not_blank(value: str) -> None:
    """Дополнительная защита от строки из одних пробелов.

    Django's blank=False отклоняет только пустую строку "" на уровне формы,
    но не строку из пробелов " " -- эта проверка закрывает оба случая.
    """
    if not value or not value.strip():
        raise ValidationError("Имя не может быть пустым.")


class Visitor(models.Model):
    """Посетитель, оставивший своё имя на главной странице.

    По условию задания модель содержит только одно поле: "name".
    """

    name = models.CharField(
        max_length=100,
        validators=[validate_not_blank],
        help_text="Имя, введённое пользователем на главной странице",
    )

    def __str__(self) -> str:
        return self.name
