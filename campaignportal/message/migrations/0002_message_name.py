# Generated by Django 3.0.6 on 2020-05-31 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='name',
            field=models.TextField(default=''),
        ),
    ]
