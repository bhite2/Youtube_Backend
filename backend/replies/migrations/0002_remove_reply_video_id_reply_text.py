# Generated by Django 4.1.7 on 2023-03-17 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('replies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='video_id',
        ),
        migrations.AddField(
            model_name='reply',
            name='text',
            field=models.CharField(default=None, max_length=500),
            preserve_default=False,
        ),
    ]
