# Generated by Django 2.2.12 on 2022-03-28 13:30

from django.db import migrations, models
import hashid_field.field


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='hash',
            field=hashid_field.field.HashidField(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', min_length=7, null=True, prefix=''),
        ),
        migrations.AddField(
            model_name='workspace',
            name='hash',
            field=hashid_field.field.HashidField(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', min_length=7, null=True, prefix=''),
        ),
        migrations.AlterField(
            model_name='document',
            name='description',
            field=models.TextField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='workspace',
            name='description',
            field=models.TextField(blank=True, max_length=250),
        ),
    ]
