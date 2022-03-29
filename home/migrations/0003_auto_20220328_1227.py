# Generated by Django 2.2.12 on 2022-03-28 12:27

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20220328_1021'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workspace',
            old_name='color',
            new_name='backcolor',
        ),
        migrations.AddField(
            model_name='workspace',
            name='forecolor',
            field=colorfield.fields.ColorField(default='#000000', image_field=None, max_length=18, samples=None),
        ),
    ]