from django.db import models
from django.db.models import DateTimeField


class Noutbuk(models.Model):
    link = models.TextField('Ссылка')
    nalicie = models.TextField('Есть в наличии')
    description = models.TextField('Описание')
    price = models.DecimalField(max_digits=12, decimal_places=2)
   # DateTimeField: DateTimeField = models.DateTimeField(
   #     auto_now_add=True,
   #     blank=True,
   #     verbose_name='Дата прихода '
   # )

    @property
    def get_absolute_url(self):
        return self.link

    def __str__(self):
        return f'{self.description[:60]} | {self.price}'

    class Meta:
        verbose_name = 'Ноутбук'
        verbose_name_plural = 'Ноутбуки'
        ordering = ['-price']