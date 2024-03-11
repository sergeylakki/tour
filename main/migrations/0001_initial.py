# Generated by Django 5.0.3 on 2024-03-05 19:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_datetime', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
                ('on_delete', models.BooleanField(default=False, verbose_name='Удалено')),
            ],
        ),
        migrations.CreateModel(
            name='MainData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='', max_length=255, verbose_name='Текст')),
                ('description', models.CharField(default='', max_length=255, verbose_name='Описание')),
                ('code', models.CharField(default='', max_length=255, verbose_name='Код')),
                ('image', models.ImageField(blank=True, null=True, upload_to='main', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Параметр',
                'verbose_name_plural': 'Основные данные сайта',
            },
        ),
        migrations.CreateModel(
            name='CategoryEvent',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.base')),
                ('name', models.CharField(max_length=10, unique=True, verbose_name='Название')),
                ('code', models.CharField(max_length=10, unique=True, verbose_name='Код')),
            ],
            options={
                'verbose_name': 'Категория тура',
                'verbose_name_plural': 'Категории туров',
            },
            bases=('main.base',),
        ),
        migrations.CreateModel(
            name='IndexCarousel',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.base')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('text', models.TextField(blank=True, default='', null=True, verbose_name='Полное описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/carousel/', verbose_name='Картинка')),
            ],
            options={
                'verbose_name': 'Карусель',
                'verbose_name_plural': 'Карусели',
            },
            bases=('main.base',),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.base')),
                ('title', models.CharField(max_length=255, verbose_name='Ф.И.О.')),
                ('text', models.TextField(blank=True, default='', null=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/teams/', verbose_name='Картинка')),
            ],
            options={
                'verbose_name': 'Участник команды',
                'verbose_name_plural': 'Команда',
            },
            bases=('main.base',),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.CharField(max_length=255, verbose_name='Кратное описание')),
                ('text', models.TextField(default='', verbose_name='Полное описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/event/', verbose_name='Картинка')),
                ('visible', models.BooleanField(default=True, verbose_name='Видимость для подписчиков')),
                ('days', models.IntegerField(verbose_name='Колличество дней')),
                ('old_price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Старая цена')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Цена в р. (0 для бесплаьного)')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_datetime', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
                ('on_delete', models.BooleanField(default=False, verbose_name='Удалено')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.categoryevent', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Тур',
                'verbose_name_plural': 'Туры',
            },
        ),
        migrations.CreateModel(
            name='EventCarousel',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.base')),
                ('title', models.CharField(max_length=255, verbose_name='День')),
                ('description', models.CharField(max_length=255, verbose_name='Кратное описание')),
                ('text', models.TextField(default='', verbose_name='Полное описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/event_courses/', verbose_name='Картинка')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.event', verbose_name='Тур')),
            ],
            options={
                'verbose_name': 'Карусель',
                'verbose_name_plural': 'Карусели туров',
            },
            bases=('main.base',),
        ),
        migrations.CreateModel(
            name='EventEatCarousel',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.base')),
                ('title', models.CharField(max_length=255, verbose_name='День')),
                ('description', models.CharField(max_length=255, verbose_name='Кратное описание')),
                ('text', models.TextField(default='', verbose_name='Полное описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/event_courses/', verbose_name='Картинка')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.event', verbose_name='Тур')),
            ],
            options={
                'verbose_name': 'Еда карусель',
                'verbose_name_plural': 'Еда карусель туров',
            },
            bases=('main.base',),
        ),
    ]
