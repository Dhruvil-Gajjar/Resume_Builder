# Generated by Django 4.0.1 on 2022-01-25 08:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('skill_id', models.CharField(default=uuid.uuid4, max_length=36, primary_key=True, serialize=False)),
                ('skill_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Skills',
                'db_table': 'skills',
                'managed': False,
            },
        ),
    ]
