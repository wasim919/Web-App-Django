# Generated by Django 2.1.2 on 2018-11-15 16:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0003_auto_20181115_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaintregister',
            name='comp_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/2018-11-15 16:45:45.834705'),
        ),
        migrations.AlterField(
            model_name='complaintregister',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 15, 16, 45, 45, 834766, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='courrier',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 15, 16, 45, 45, 835757, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='hostelleave',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 15, 16, 45, 45, 833951, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='selfhelpgroup',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 15, 16, 45, 45, 837462, tzinfo=utc)),
        ),
    ]
