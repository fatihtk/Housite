# Generated by Django 2.1.dev20171223092632 on 2018-01-05 23:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0009_houses_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='houses',
            name='author',
        ),
    ]
