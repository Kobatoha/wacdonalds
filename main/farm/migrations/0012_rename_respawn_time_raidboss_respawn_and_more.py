# Generated by Django 4.1.7 on 2023-02-26 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0011_remove_raidboss_respawn_farmraidboss_respawn_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='raidboss',
            old_name='respawn_time',
            new_name='respawn',
        ),
        migrations.AlterField(
            model_name='farmraidboss',
            name='respawn',
            field=models.TimeField(null=True, verbose_name='Время возрождения'),
        ),
    ]
