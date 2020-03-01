# Generated by Django 3.0.3 on 2020-03-01 10:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserCredentials',
            fields=[
                ('user_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('email', models.EmailField(blank=True, help_text='Enter a valid email address', max_length=70, null=True, unique=True)),
                ('password', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
