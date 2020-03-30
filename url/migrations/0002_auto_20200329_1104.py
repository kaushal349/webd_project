# Generated by Django 3.0.4 on 2020-03-29 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='url',
            name='shorten_url',
        ),
        migrations.AddField(
            model_name='url',
            name='shortcode',
            field=models.CharField(default='abc', max_length=15),
        ),
        migrations.AlterField(
            model_name='url',
            name='actual_url',
            field=models.CharField(max_length=220),
        ),
    ]
