# Generated by Django 4.2.2 on 2023-07-06 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('copies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='copy',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]
