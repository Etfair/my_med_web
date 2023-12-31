# Generated by Django 4.2.6 on 2023-11-08 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='имя')),
                ('content', models.TextField(blank=True, max_length=500, null=True, verbose_name='текст')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('view_count', models.PositiveIntegerField(default=0, verbose_name='количество просмотров')),
            ],
            options={
                'verbose_name': 'Блог>',
                'verbose_name_plural': 'Блоги',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=50, verbose_name='название')),
                ('content', models.TextField(verbose_name='описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('view_count', models.PositiveIntegerField(default=0, verbose_name='количество просмотров')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='имя')),
                ('email', models.CharField(blank=True, max_length=100, null=True, verbose_name='Email')),
                ('message', models.TextField(blank=True, max_length=500, null=True, verbose_name='отзыв')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='main.service', verbose_name='услуга')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
