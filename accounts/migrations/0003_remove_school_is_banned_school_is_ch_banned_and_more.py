# Generated by Django 4.1.1 on 2022-10-04 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_school_is_banned'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='is_banned',
        ),
        migrations.AddField(
            model_name='school',
            name='is_ch_banned',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='school',
            name='is_pac_banned',
            field=models.BooleanField(default=False),
        ),
    ]
