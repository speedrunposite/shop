# Generated by Django 3.1.1 on 2021-08-18 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20210809_1542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pavingslab',
            name='width',
        ),
        migrations.RemoveField(
            model_name='tile',
            name='width',
        ),
    ]