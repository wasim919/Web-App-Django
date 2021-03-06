# Generated by Django 2.1.2 on 2018-11-15 16:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mess', '0003_auto_20181115_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messfeedback',
            name='comp_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/2018-11-15 16:45:45.845877'),
        ),
        migrations.AlterField(
            model_name='messfeedback',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 15, 16, 45, 45, 845916, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='messleave',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 15, 16, 45, 45, 842030, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='messrefund',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 15, 16, 45, 45, 842941, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderhistorymess',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 15, 16, 45, 45, 844209, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderlistmess',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 15, 16, 45, 45, 845001, tzinfo=utc)),
        ),
    ]
