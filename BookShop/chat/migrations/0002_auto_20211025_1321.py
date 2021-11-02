# Generated by Django 3.2.7 on 2021-10-25 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'сообщение', 'verbose_name_plural': 'сообщения'},
        ),
        migrations.AlterModelOptions(
            name='room',
            options={'verbose_name': 'комната', 'verbose_name_plural': 'коинаты'},
        ),
        migrations.AlterField(
            model_name='message',
            name='room',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='message',
            name='value',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
