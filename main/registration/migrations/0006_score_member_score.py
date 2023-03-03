# Generated by Django 4.1.7 on 2023-02-25 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_remove_member_twink_member_main'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.PositiveIntegerField(default=0, verbose_name='ДЦП очки')),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='score',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='registration.score'),
        ),
    ]