# Generated by Django 3.2.12 on 2022-08-10 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tag',
        ),
    ]