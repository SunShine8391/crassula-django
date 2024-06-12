# Generated by Django 4.1.5 on 2023-04-06 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='members')),
            ],
            options={
                'verbose_name': 'Member',
                'verbose_name_plural': 'Members',
                'ordering': ('full_name',),
            },
        ),
        migrations.AddField(
            model_name='event',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='members',
            field=models.ManyToManyField(blank=True, null=True, to='events.member'),
        ),
    ]