# Generated by Django 5.0.6 on 2024-06-08 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_product_company_alter_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.UUIDField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
