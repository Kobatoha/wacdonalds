# Generated by Django 4.1.7 on 2023-02-26 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0009_remove_member_score_clanmember_score'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Member',
            new_name='Character',
        ),
        migrations.RenameField(
            model_name='clanmember',
            old_name='character',
            new_name='characters',
        ),
    ]
