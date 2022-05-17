from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=24, blank=False, verbose_name='Категория')
    slug = models.SlugField(max_length=24)

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.category_name}'


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.CharField(max_length=1500)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return f'/{self.id}'

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class Reaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=300)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    published = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = 'Отклик'
        verbose_name_plural = 'Отклики'

    def get_absolute_url(self):
        return f'../{self.message.id}'

