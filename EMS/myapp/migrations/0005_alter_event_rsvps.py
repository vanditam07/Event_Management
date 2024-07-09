# Generated by Django 5.0.1 on 2024-02-29 16:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_profile'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='rsvps',
            field=models.ManyToManyField(blank=True, related_name='rsvped_events', to=settings.AUTH_USER_MODEL),
        ),
    ]
