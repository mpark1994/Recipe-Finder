# Generated by Django 4.1.1 on 2022-10-13 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_home', '0002_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='subject',
            field=models.CharField(default='hello', max_length=255),
            preserve_default=False,
        ),
    ]
