# Generated by Django 4.2.4 on 2023-08-30 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_partnercompanylogo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='video_link',
        ),
        migrations.AddField(
            model_name='banner',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='banner_videos/'),
        ),
    ]