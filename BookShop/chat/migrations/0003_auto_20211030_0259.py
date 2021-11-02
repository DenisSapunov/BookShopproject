# Generated by Django 3.2.7 on 2021-10-29 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20211025_1321'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'verbose_name': 'Комната', 'verbose_name_plural': 'Комнаты'},
        ),
        migrations.AlterField(
            model_name='message',
            name='room',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='message',
            name='value',
            field=models.TextField(),
        ),
    ]
