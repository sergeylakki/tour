# Generated by Django 5.0.3 on 2024-03-11 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='comment',
            field=models.TextField(blank=True, default='', max_length=255, verbose_name='Комментарий'),
        ),
    ]
