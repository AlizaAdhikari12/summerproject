# Generated by Django 4.1.3 on 2023-05-23 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lishapp', '0034_carousel_description_alter_product_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='mfgdate',
        ),
    ]