# Generated by Django 4.1.5 on 2023-04-05 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promote', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('live', 'Live'), ('ended', 'Ended'), ('upcoming', 'Upcoming')], max_length=100)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('duration', models.CharField(blank=True, max_length=100, null=True)),
                ('stand', models.CharField(blank=True, max_length=255, null=True)),
                ('logo', models.ImageField(upload_to='events')),
                ('about_top', models.TextField(blank=True, null=True)),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='events')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='events')),
                ('about_bottom', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
                'ordering': ('-date_start',),
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('terms_accepted', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
            ],
            options={
                'verbose_name': 'Booking',
                'verbose_name_plural': 'Bookings',
                'ordering': ('-date',),
            },
        ),
    ]