# Generated by Django 4.1.3 on 2023-05-25 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lishapp', '0039_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default=False, max_length=100, unique=True),
        ),
    ]
