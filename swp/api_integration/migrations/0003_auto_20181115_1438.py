# Generated by Django 2.1.2 on 2018-11-15 14:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api_integration', '0002_auto_20181115_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 15, 14, 38, 45, 113560, tzinfo=utc)),
        ),
    ]
