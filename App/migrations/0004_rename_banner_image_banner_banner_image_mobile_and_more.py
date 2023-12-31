# Generated by Django 4.2.4 on 2023-08-29 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_delete_pagemetatext_remove_pagemeta_seo_script_one_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banner',
            old_name='banner_image',
            new_name='banner_image_mobile',
        ),
        migrations.AddField(
            model_name='banner',
            name='banner_image_desktop',
            field=models.ImageField(blank=True, null=True, upload_to='banner_images/'),
        ),
        migrations.AddField(
            model_name='banner',
            name='banner_image_tablet',
            field=models.ImageField(blank=True, null=True, upload_to='banner_images/'),
        ),
    ]
