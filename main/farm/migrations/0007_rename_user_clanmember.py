# Generated by Django 4.1.7 on 2023-02-26 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0006_user_character_alter_farmraidboss_drop_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='ClanMember',
        ),
    ]