# Generated by Django 4.1.7 on 2023-02-26 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0008_alter_farmraidboss_party_members'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='score',
        ),
        migrations.AddField(
            model_name='clanmember',
            name='score',
            field=models.IntegerField(default=0, verbose_name='Score'),
        ),
    ]
