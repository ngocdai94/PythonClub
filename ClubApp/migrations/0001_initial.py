# Generated by Django 3.0.5 on 2020-04-18 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClubInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clubname', models.CharField(max_length=255)),
                ('clubdescription', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'clubinformations',
                'db_table': 'clubinformation',
            },
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meetingtitle', models.CharField(max_length=255)),
                ('meetingdate', models.DateField()),
                ('meetingtime', models.TimeField()),
                ('meetinglocation', models.CharField(max_length=255)),
                ('meetagenda', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'meetings',
                'db_table': 'meeting',
            },
        ),
    ]
