# Generated by Django 3.2.7 on 2021-11-01 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_auto_20211102_0218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='num_pages',
            field=models.IntegerField(null=True, verbose_name='Количество страниц'),
        ),
        migrations.AlterField(
            model_name='book',
            name='pub_year',
            field=models.IntegerField(null=True, verbose_name='Год публикации'),
        ),
    ]