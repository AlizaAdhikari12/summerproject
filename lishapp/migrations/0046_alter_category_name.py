# Generated by Django 4.1.3 on 2023-05-26 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lishapp', '0045_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(error_messages={'unique': 'Custom unique constraint failed.'}, max_length=100, unique=True),
        ),
    ]
