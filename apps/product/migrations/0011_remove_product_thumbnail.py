# Generated by Django 3.1.5 on 2021-02-15 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_delete_mymodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='thumbnail',
        ),
    ]
