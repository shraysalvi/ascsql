# Generated by Django 4.1.2 on 2022-10-12 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_product_organization'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reports',
            new_name='Report',
        ),
    ]
