# Generated by Django 4.1 on 2022-09-19 05:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('serial_num', models.SmallIntegerField()),
                ('question', models.TextField()),
                ('answer', models.CharField(max_length=100)),
            ],
        ),
    ]
