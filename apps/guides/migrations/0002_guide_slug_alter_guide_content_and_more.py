# Generated by Django 4.2 on 2023-04-23 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guides', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guide',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AlterField(
            model_name='guide',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='guide',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='guide',
            name='modified_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='guide',
            name='published_date',
            field=models.DateTimeField(null=True),
        ),
    ]
