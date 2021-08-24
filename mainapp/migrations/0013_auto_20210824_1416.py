# Generated by Django 3.2.4 on 2021-08-24 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_auto_20210824_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pavingslab',
            name='max_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='Цена до'),
        ),
        migrations.AlterField(
            model_name='pavingstone',
            name='max_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='Цена до'),
        ),
        migrations.AlterField(
            model_name='stair',
            name='max_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='Цена до'),
        ),
        migrations.AlterField(
            model_name='tile',
            name='max_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='Цена до'),
        ),
    ]
