# Generated by Django 4.1.1 on 2022-10-03 15:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('crypt_hunt', '0011_question_question_uuid_alter_question_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='question_uuid',
        ),
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
