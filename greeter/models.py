from django.db import models


# Модель посетителя. По заданию — только одно поле: имя.
class Visitor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
