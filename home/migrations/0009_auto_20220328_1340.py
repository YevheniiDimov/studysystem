# Generated by Django 2.2.12 on 2022-03-28 13:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20220328_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
