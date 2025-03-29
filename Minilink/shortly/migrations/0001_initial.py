# Generated by Django 5.1.7 on 2025-03-29 07:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='linkup', to=settings.AUTH_USER_MODEL, verbose_name='ارسال کننده')),
            ],
        ),
    ]
