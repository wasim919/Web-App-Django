# Generated by Django 2.1.2 on 2018-12-10 15:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api_integration', '0018_merge_20181210_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 15, 45, 51, 27167, tzinfo=utc)),
        ),
    ]
