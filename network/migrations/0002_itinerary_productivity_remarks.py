# Generated by Django 3.2.4 on 2021-08-01 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activityid', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Productivity',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('activity_title', models.CharField(max_length=1024)),
                ('activity_datetime', models.CharField(max_length=1024)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('estimatedcost', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Remarks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1024)),
                ('activityid', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
