# Generated by Django 2.1.2 on 2018-10-24 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0004_auto_20181024_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaintregister',
            name='comp_img',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/'),
        ),
    ]