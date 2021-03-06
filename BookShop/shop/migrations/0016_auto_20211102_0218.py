# Generated by Django 3.2.7 on 2021-11-01 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(null=True, related_name='books', to='shop.Author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(null=True, related_name='books', to='shop.Category'),
        ),
    ]
