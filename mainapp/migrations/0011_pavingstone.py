# Generated by Django 3.1.1 on 2021-08-22 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_auto_20210822_0027'),
    ]

    operations = [
        migrations.CreateModel(
            name='PavingStone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('min_price', models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='Цена от')),
                ('max_price', models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='Цена до')),
                ('size', models.CharField(max_length=255, verbose_name='Размер')),
                ('unit', models.CharField(max_length=255, verbose_name='Единица измерения')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]