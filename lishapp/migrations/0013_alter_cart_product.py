# Generated by Django 4.1.3 on 2023-05-13 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lishapp', '0012_remove_cart_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='product',
            field=models.TextField(default={'objects=[]'}),
        ),
    ]
