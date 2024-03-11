from django.contrib.auth.models import User
from django.db import models


class Base(models.Model):
    create_datetime = models.DateTimeField('Дата создания', auto_now_add=True)
    update_datetime = models.DateTimeField('Дата создания', auto_now=True)
    on_delete = models.BooleanField('Удалено', default=False)


class MainData(models.Model):
    title = models.TextField('Текст', max_length=255, default='')
    description = models.CharField('Описание', max_length=255, default='')
    code = models.CharField('Код', max_length=255, default='')
    image = models.ImageField('Фото', blank=True, null=True, upload_to='main')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Параметр'
        verbose_name_plural = 'Основные данные сайта'


class Team(Base):
    title = models.CharField('Ф.И.О.', max_length=255)
    text = models.TextField('Описание', default='', blank=True, null=True)
    image = models.ImageField('Картинка', upload_to='media/teams/', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Участник команды'
        verbose_name_plural = 'Команда'


class IndexCarousel(Base):
    title = models.CharField('Заголовок', max_length=255)
    text = models.TextField('Полное описание', default='', blank=True, null=True)
    image = models.ImageField('Картинка', upload_to='media/carousel/', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Карусель'
        verbose_name_plural = 'Карусели'


class CategoryEvent(Base):
    name = models.CharField('Название', max_length=10, unique=True)
    code = models.CharField('Код', max_length=10, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория тура'
        verbose_name_plural = 'Категории туров'


class Event(models.Model):
    title = models.CharField('Название', max_length=255)
    description = models.CharField('Кратное описание', max_length=255)
    text = models.TextField('Полное описание', default='')
    image = models.ImageField('Картинка', upload_to='media/event/', blank=True, null=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.SET_NULL, blank=True, null=True)
    visible = models.BooleanField('Видимость для подписчиков', default=True)
    category = models.ForeignKey(CategoryEvent, verbose_name='Категория', on_delete=models.SET_NULL,
                                 blank=True, null=True)
    days = models.IntegerField('Колличество дней')
    old_price = models.DecimalField('Старая цена', decimal_places=2, max_digits=10, default=0)
    price = models.DecimalField('Цена в р. (0 для бесплаьного)', decimal_places=2, max_digits=10, default=0)
    eat = models.TextField('Еда (меню)', null=True, blank=True, default='')
    сonditions = models.TextField('Условия', null=True, blank=True, default='')
    sale = models.BooleanField('Акция', null=False, blank=True, default=False)
    # Системные настройки
    create_datetime = models.DateTimeField('Дата создания', auto_now_add=True)
    update_datetime = models.DateTimeField('Дата создания', auto_now=True)
    on_delete = models.BooleanField('Удалено', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'


class EventCarousel(Base):
    title = models.CharField('Заголовок', max_length=255, blank=True, null=False, default='')
    description = models.CharField('Кратное описание', max_length=255,  blank=True, null=False, default='')
    text = models.TextField('Полное описание', default='', blank=True, null=False)
    image = models.ImageField('Картинка', upload_to='media/event_courses/', blank=True, null=True)
    event = models.ForeignKey(Event, verbose_name='Тур', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Карусель'
        verbose_name_plural = 'Карусели туров'


class EventProgram(Base):
    title = models.CharField('День', max_length=255)
    text = models.TextField('Полное описание', default='')
    image = models.ImageField('Картинка', upload_to='media/event_courses/', blank=True, null=True)
    event = models.ForeignKey(Event, verbose_name='Тур', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Программа по дням'
        verbose_name_plural = 'Программы по дням'


class EventEat(Base):
    title = models.CharField('День', max_length=255)
    image = models.ImageField('Картинка', upload_to='media/event_courses/', blank=True, null=True)
    event = models.ForeignKey(Event, verbose_name='Тур', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фото еды'
        verbose_name_plural = 'Фото еды'


class Author(Base):
    title = models.CharField('Ф.И.О', max_length=255)
    description = models.CharField('Кратное описание', max_length=255)
    text = models.TextField('Полное описание', default='')
    image = models.ImageField('Картинка', upload_to='media/event_courses/', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class AboutUs(Base):
    title = models.CharField('Заголовок', max_length=255)
    text = models.TextField('Полное описание', default='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'


class Client(Base):
    name = models.CharField('Имя', max_length=255)
    email = models.CharField('Почта', max_length=255, blank=True, default='')
    phone = models.CharField('Телефон', max_length=255)
    comment = models.TextField('Комментарий', max_length=255, blank=True, default='')
    event = models.ForeignKey(Event, verbose_name='Тур', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.event.title}'

    class Meta:
        verbose_name = 'Бронь'
        verbose_name_plural = 'Бронь'