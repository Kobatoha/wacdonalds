# Generated by Django 4.1.7 on 2023-02-25 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_score_member_score'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Member',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
        migrations.DeleteModel(
            name='Score',
        ),
    ]