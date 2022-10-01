# Generated by Django 4.1.1 on 2022-10-01 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crypt_hunt', '0002_alter_question_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contents', models.CharField(max_length=1000)),
                ('status', models.CharField(choices=[('ODT', 'Outdated'), ('COR', 'Correct'), ('INC', 'Incorrect')], default='INC', max_length=3)),
                ('time_submitted', models.DateTimeField(auto_now_add=True)),
                ('school', models.CharField(max_length=100)),
                ('user_id', models.CharField(default=None, max_length=100, null=True)),
                ('ip_address', models.CharField(max_length=100)),
                ('for_question', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='crypt_hunt.question')),
            ],
        ),
    ]
