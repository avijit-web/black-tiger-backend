# Generated by Django 4.2.4 on 2023-08-28 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_banner'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PageMetaText',
        ),
        migrations.RemoveField(
            model_name='pagemeta',
            name='seo_script_one',
        ),
        migrations.RemoveField(
            model_name='pagemeta',
            name='seo_script_two',
        ),
    ]
