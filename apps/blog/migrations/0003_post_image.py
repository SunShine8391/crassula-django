# Generated by Django 4.1.4 on 2022-12-15 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_date_edit_alter_post_date_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='media/blog/posts'),
        ),
    ]
