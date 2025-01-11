from django.db import models

class Noutbuk(models.Model):
    link = models.TextField('Ссылка')
    nalicie = models.TextField('Есть в наличии')
    description = models.TextField('Описание')
    price = models.DecimalField(max_digits=12, decimal_places=2)
