# Generated by Django 5.0.3 on 2024-03-06 08:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventcarousel',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Заголовок'),
        ),
        migrations.CreateModel(
            name='EventProgramm',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.base')),
                ('title', models.CharField(max_length=255, verbose_name='День')),
                ('text', models.TextField(default='', verbose_name='Полное описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/event_courses/', verbose_name='Картинка')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.event', verbose_name='Тур')),
            ],
            options={
                'verbose_name': 'Программа по дням',
                'verbose_name_plural': 'Программы по дням',
            },
            bases=('main.base',),
        ),
    ]