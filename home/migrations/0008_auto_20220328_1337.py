# Generated by Django 2.2.12 on 2022-03-28 13:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20220328_1334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='hash',
        ),
        migrations.RemoveField(
            model_name='workspace',
            name='hash',
        ),
        migrations.AlterField(
            model_name='workspace',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
