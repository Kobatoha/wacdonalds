# Generated by Django 4.1.7 on 2023-02-26 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0007_rename_user_clanmember'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmraidboss',
            name='party_members',
            field=models.ManyToManyField(blank=True, to='farm.clanmember'),
        ),
    ]
