# Generated by Django 5.1.7 on 2025-03-29 16:16

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortly', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='text',
        ),
        migrations.AddField(
            model_name='link',
            name='url_long',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='link',
            name='url_short',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
