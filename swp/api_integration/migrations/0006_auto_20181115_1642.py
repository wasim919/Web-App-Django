# Generated by Django 2.1.2 on 2018-11-15 16:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api_integration', '0005_auto_20181115_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 15, 16, 42, 26, 480840, tzinfo=utc)),
        ),
    ]
