# Generated by Django 4.2.2 on 2023-07-01 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=50)),
                ('sinopse', models.TextField(default=None, null=True)),
                ('coverImage', models.CharField(default=None, max_length=50, null=True)),
                ('pageQuantity', models.IntegerField()),
            ],
        ),
    ]
