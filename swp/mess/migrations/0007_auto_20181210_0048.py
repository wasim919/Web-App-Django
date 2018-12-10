# Generated by Django 2.1.2 on 2018-12-09 19:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mess', '0006_merge_20181116_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messfeedback',
            name='comp_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/2018-12-10 00:48:02.196043'),
        ),
        migrations.AlterField(
            model_name='messfeedback',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 9, 19, 18, 2, 196043, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='messleave',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 9, 19, 18, 2, 193045, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='messrefund',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 9, 19, 18, 2, 193045, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderhistorymess',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 9, 19, 18, 2, 195043, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderlistmess',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 9, 19, 18, 2, 196043, tzinfo=utc)),
        ),
    ]