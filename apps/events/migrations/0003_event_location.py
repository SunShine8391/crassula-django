# Generated by Django 4.1.5 on 2023-04-06 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]