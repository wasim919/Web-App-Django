# Generated by Django 2.1.2 on 2018-12-10 07:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0008_auto_20181210_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaintregister',
            name='comp_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/2018-12-10 13:16:36.227743'),
        ),
        migrations.AlterField(
            model_name='complaintregister',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 7, 46, 36, 227743, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='courrier',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 7, 46, 36, 228743, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='hostelleave',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 7, 46, 36, 227743, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='selfhelpgroup',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 7, 46, 36, 229743, tzinfo=utc)),
        ),
    ]
