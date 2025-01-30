# Generated by Django 5.1.5 on 2025-01-27 11:44

import common.file_path_renamer
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_variation_options_alter_variation_table_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(unique=True, upload_to=common.file_path_renamer.PathAndRename('products/images')),
        ),
    ]
