# Generated by Django 4.1.1 on 2022-10-13 07:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apps_home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_id', models.IntegerField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favoriter', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
