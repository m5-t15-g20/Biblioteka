# Generated by Django 4.2.2 on 2023-07-11 08:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('copies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_close', models.BooleanField(default=False)),
                ('expire_date', models.DateField(default=datetime.date(2023, 7, 18))),
                ('lending_date', models.DateField()),
                ('copy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leadings', to='copies.copy')),
            ],
        ),
    ]
