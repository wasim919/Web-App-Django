# Generated by Django 2.1.2 on 2018-11-15 14:39

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api_integration', '0004_auto_20181115_1439'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=45, unique=True)),
                ('item_type', models.CharField(max_length=45)),
                ('cost', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2018, 11, 15, 14, 38, 59, 490166, tzinfo=utc))),
                ('created_at', models.DateField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=45, null=True)),
                ('modified_at', models.DateField(blank=True, null=True)),
                ('modified_by', models.CharField(blank=True, max_length=45, null=True)),
                ('delete', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ManualOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_name', models.CharField(max_length=45)),
                ('order_type', models.CharField(max_length=45)),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2018, 11, 15, 14, 38, 59, 490674, tzinfo=utc))),
                ('created_at', models.DateField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=45, null=True)),
                ('modified_at', models.DateField(blank=True, null=True)),
                ('modified_by', models.CharField(blank=True, max_length=45, null=True)),
                ('delete', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='OrderHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2018, 11, 15, 14, 38, 59, 492174, tzinfo=utc))),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=45, null=True)),
                ('modified_at', models.DateField(blank=True, null=True)),
                ('modified_by', models.CharField(blank=True, max_length=45, null=True)),
                ('delete', models.BooleanField(default=0)),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='orders.Items')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api_integration.Student')),
            ],
        ),
        migrations.CreateModel(
            name='OrderList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2018, 11, 15, 14, 38, 59, 491387, tzinfo=utc))),
                ('created_at', models.DateField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=45, null=True)),
                ('modified_at', models.DateField(blank=True, null=True)),
                ('modified_by', models.CharField(blank=True, max_length=45, null=True)),
                ('delete', models.BooleanField(default=0)),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='orders.Items')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api_integration.Student')),
            ],
        ),
    ]
