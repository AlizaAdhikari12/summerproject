# Generated by Django 4.1.3 on 2023-05-15 20:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lishapp', '0026_alter_product_price_alter_product_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='created_at',
            new_name='created',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='product_qty',
        ),
        migrations.AddField(
            model_name='cart',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='product',
            field=models.TextField(blank=True, default={'objects': []}, null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
