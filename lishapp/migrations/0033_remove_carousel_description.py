# Generated by Django 4.1.3 on 2023-05-21 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lishapp', '0032_alter_userprofile_phoneno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carousel',
            name='description',
        ),
    ]
