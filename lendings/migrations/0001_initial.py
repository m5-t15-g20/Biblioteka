# Generated by Django 4.2.2 on 2023-07-01 21:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_avaliable', models.BooleanField(default=True)),
                ('expire_date', models.DateField()),
                ('lending_date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leadings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
