# Generated by Django 3.2.7 on 2021-10-29 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_alter_userbookrate_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=300, unique=True, verbose_name='SLUG'),
        ),
    ]
