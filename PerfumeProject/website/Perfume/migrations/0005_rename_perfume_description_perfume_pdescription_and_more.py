# Generated by Django 5.0.2 on 2024-02-18 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Perfume', '0004_perfume_image_perfume_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfume',
            old_name='Perfume_Description',
            new_name='PDescription',
        ),
        migrations.RenameField(
            model_name='perfume',
            old_name='Perfume_name',
            new_name='Pname',
        ),
    ]
