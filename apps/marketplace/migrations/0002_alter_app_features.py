# Generated by Django 4.1.5 on 2023-02-23 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0001_initial'),
        ('marketplace', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='features',
            field=models.ManyToManyField(blank=True, to='features.feature'),
        ),
    ]
