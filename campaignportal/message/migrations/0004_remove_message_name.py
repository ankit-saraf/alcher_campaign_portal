# Generated by Django 3.0.6 on 2020-06-02 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0003_auto_20200601_1449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='name',
        ),
    ]