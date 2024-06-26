# Generated by Django 4.2 on 2023-04-23 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField()),
                ('content', models.TextField()),
                ('published_date', models.DateTimeField()),
                ('modified_date', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Guide',
                'verbose_name_plural': 'Guide',
                'ordering': ('-published_date',),
            },
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(blank=True, max_length=255, null=True)),
                ('answer', models.TextField()),
                ('guide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guides.guide')),
            ],
            options={
                'verbose_name': 'FAQ',
                'verbose_name_plural': 'FAQ',
                'ordering': ('question',),
            },
        ),
    ]
