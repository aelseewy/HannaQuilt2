# Generated by Django 3.1.5 on 2021-02-08 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_remove_product_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]