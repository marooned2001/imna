# Generated by Django 5.0.2 on 2024-05-09 11:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField()),
                ('user_email', models.EmailField(max_length=254)),
                ('comment_text', models.TextField()),
                ('new', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newspaper.news')),
            ],
        ),
    ]
