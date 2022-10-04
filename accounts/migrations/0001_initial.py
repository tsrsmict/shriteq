# Generated by Django 4.1.1 on 2022-10-04 13:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=100)),
                ('question_num', models.SmallIntegerField(default=1, null=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('is_ch_banned', models.BooleanField(default=False)),
                ('is_pac_banned', models.BooleanField(default=False)),
                ('account', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]