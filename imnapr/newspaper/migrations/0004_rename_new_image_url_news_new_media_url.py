# Generated by Django 5.0.2 on 2024-05-09 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0003_alter_news_new_image_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='new_image_url',
            new_name='new_media_url',
        ),
    ]