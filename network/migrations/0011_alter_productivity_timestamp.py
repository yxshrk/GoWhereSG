# Generated by Django 3.2.4 on 2021-08-06 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0010_watchlist_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productivity',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
