# Generated by Django 5.0.2 on 2024-02-18 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Perfume', '0005_rename_perfume_description_perfume_pdescription_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Perfume',
        ),
    ]