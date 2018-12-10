# Generated by Django 2.1.2 on 2018-12-10 13:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mess', '0010_auto_20181210_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messfeedback',
            name='comp_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/2018-12-10 18:58:20.450159'),
        ),
        migrations.AlterField(
            model_name='messfeedback',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 13, 28, 20, 450159, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='messleave',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 13, 28, 20, 445158, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='messrefund',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 13, 28, 20, 445158, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderhistorymess',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 13, 28, 20, 450159, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderlistmess',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 13, 28, 20, 450159, tzinfo=utc)),
        ),
    ]
