# Generated by Django 3.2.4 on 2021-08-03 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_productivity_activity_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='productivity',
            name='category',
            field=models.CharField(max_length=1024, null=True),
        ),
    ]
