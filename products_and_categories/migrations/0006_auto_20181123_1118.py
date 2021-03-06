# Generated by Django 2.1.3 on 2018-11-23 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_and_categories', '0005_auto_20181122_1837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='categoriesId',
        ),
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='products', to='products_and_categories.Category'),
        ),
    ]
