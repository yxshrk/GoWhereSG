# Generated by Django 3.2.4 on 2021-08-03 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_productivity_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='productivity',
            name='link',
            field=models.CharField(max_length=1024, null=True),
        ),
    ]
