# Generated by Django 4.1.7 on 2023-02-26 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0004_dropraidboss_raidboss_respawn_alter_raidboss_level_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя игрока')),
            ],
        ),
        migrations.RemoveField(
            model_name='dropraidboss',
            name='accessoire',
        ),
        migrations.RemoveField(
            model_name='dropraidboss',
            name='another',
        ),
        migrations.RemoveField(
            model_name='dropraidboss',
            name='book',
        ),
        migrations.RemoveField(
            model_name='dropraidboss',
            name='weapon',
        ),
        migrations.AddField(
            model_name='dropraidboss',
            name='price',
            field=models.PositiveBigIntegerField(default=100, verbose_name='Стоимость предмета +- в L монетах'),
        ),
        migrations.AddField(
            model_name='dropraidboss',
            name='title',
            field=models.CharField(db_index=True, max_length=100, null=True, verbose_name='Предмет'),
        ),
        migrations.AlterField(
            model_name='member',
            name='nickname',
            field=models.CharField(max_length=100, verbose_name='Имя пользователя'),
        ),
        migrations.AddField(
            model_name='member',
            name='master',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='farm.user'),
        ),
    ]
