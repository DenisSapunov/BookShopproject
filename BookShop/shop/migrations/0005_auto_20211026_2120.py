# Generated by Django 3.2.7 on 2021-10-26 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_book_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='write_year',
        ),
        migrations.AlterField(
            model_name='book',
            name='availability',
            field=models.BooleanField(default=True, verbose_name='Наличие'),
        ),
    ]
