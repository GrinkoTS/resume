# Generated by Django 3.2.20 on 2023-08-03 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100, verbose_name='Название фирмы')),
                ('job_title', models.CharField(max_length=100, verbose_name='Должность')),
                ('date', models.CharField(max_length=100, verbose_name='Годы работы')),
                ('full_text', models.TextField(verbose_name='Описание')),
            ],
        ),
    ]
