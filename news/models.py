from django.db import models

class Artiles(models.Model):
    title = models.CharField('Название фирмы', max_length=100, default='')
    job_title = models.CharField('Должность', max_length=100)
    date = models.CharField('Годы работы', max_length=100)
    full_text = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фирма'
        verbose_name_plural = 'Фирмы'
