# Generated by Django 4.1.1 on 2022-10-13 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_home', '0003_comment_email_comment_subject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comments',
            new_name='comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
