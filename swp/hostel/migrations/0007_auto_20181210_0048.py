# Generated by Django 2.1.2 on 2018-12-09 19:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0006_merge_20181116_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaintregister',
            name='comp_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/2018-12-10 00:48:02.186049'),
        ),
        migrations.AlterField(
            model_name='complaintregister',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 9, 19, 18, 2, 186049, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='courrier',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 9, 19, 18, 2, 187049, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='hostelleave',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 9, 19, 18, 2, 185050, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='selfhelpgroup',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 9, 19, 18, 2, 188048, tzinfo=utc)),
        ),
    ]
