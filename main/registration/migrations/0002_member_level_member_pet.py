# Generated by Django 4.1.7 on 2023-02-25 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='level',
            field=models.IntegerField(default=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='pet',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
