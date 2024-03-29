# Generated by Django 5.0.3 on 2024-03-11 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_event_sale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventcarousel',
            name='description',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Кратное описание'),
        ),
        migrations.AlterField(
            model_name='eventcarousel',
            name='text',
            field=models.TextField(blank=True, default='', verbose_name='Полное описание'),
        ),
        migrations.AlterField(
            model_name='eventcarousel',
            name='title',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Заголовок'),
        ),
    ]
