# Generated by Django 2.2.1 on 2019-05-15 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_blogmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogmodel',
            name='blog_id',
        ),
    ]
