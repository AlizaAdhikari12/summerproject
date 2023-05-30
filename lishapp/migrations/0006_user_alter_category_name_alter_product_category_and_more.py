# Generated by Django 4.1.3 on 2023-04-17 17:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lishapp', '0005_alter_category_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=False, max_length=200)),
                ('phone_no', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default=True, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='lishapp.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='costperpro',
            field=models.CharField(blank=True, default=False, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(default=False, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='mfgdate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default=False, max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(default=False, max_length=100),
        ),
    ]