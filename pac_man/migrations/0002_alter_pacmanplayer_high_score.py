# Generated by Django 4.1 on 2022-09-17 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pac_man', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacmanplayer',
            name='high_score',
            field=models.IntegerField(default=0),
        ),
    ]
