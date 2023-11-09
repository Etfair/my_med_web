from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    """Класс модели категорий"""
    name = models.CharField(max_length=50, verbose_name='Категория')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Service(models.Model):
    """Класс модели услуг"""
    service_name = models.CharField(max_length=50, verbose_name='название')
    content = models.TextField(verbose_name='описание')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='категория')
    image = models.ImageField(upload_to='images/', **NULLABLE)
    view_count = models.PositiveIntegerField(verbose_name='количество просмотров', default=0)

    def __str__(self):
        return f'{self.service_name}'

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Comment(models.Model):
    """Класс модели комментариев"""
    name = models.CharField(max_length=50, **NULLABLE, verbose_name='имя')
    email = models.CharField(max_length=100, **NULLABLE, verbose_name='Email')
    message = models.TextField(max_length=500, **NULLABLE, verbose_name='отзыв')
    create_at = models.DateTimeField(auto_now_add=True, **NULLABLE, verbose_name='Дата создания')
    service = models.ForeignKey('Service', related_name="comment", **NULLABLE, on_delete=models.CASCADE,
                                verbose_name='услуга')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Blog(models.Model):
    """Класс модели медицинского блога"""
    name = models.CharField(max_length=50, **NULLABLE, verbose_name='имя')
    content = models.TextField(max_length=500, **NULLABLE, verbose_name='текст')
    image = models.ImageField(upload_to='images/', **NULLABLE)
    create_at = models.DateTimeField(auto_now_add=True, **NULLABLE, verbose_name='Дата создания')
    view_count = models.PositiveIntegerField(verbose_name='количество просмотров', default=0)

    class Meta:
        verbose_name = 'Блог>'
        verbose_name_plural = 'Блоги'
