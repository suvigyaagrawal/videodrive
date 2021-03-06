# Generated by Django 3.0.6 on 2020-05-09 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='YoutubeCredentials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=40)),
                ('api_key', models.CharField(max_length=40)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
