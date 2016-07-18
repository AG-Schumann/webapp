# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('controller', models.TextField(null=True, blank=True)),
                ('status', models.TextField(null=True, blank=True)),
                ('connection', models.CharField(max_length=3, null=True, blank=True)),
                ('number_of_data', models.IntegerField(null=True, blank=True)),
                ('readout_interval', models.IntegerField(null=True, blank=True)),
                ('address1', models.TextField(null=True, blank=True)),
                ('address2', models.TextField(null=True, blank=True)),
                ('alarm_status', models.TextField(null=True, blank=True)),
                ('alarm_low1', models.FloatField(null=True, blank=True)),
                ('alarm_low2', models.FloatField(null=True, blank=True)),
                ('alarm_high1', models.FloatField(null=True, blank=True)),
                ('alarm_high2', models.FloatField(null=True, blank=True)),
            ],
            options={
                'db_table': 'config',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ConfigHistory',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('datetime', models.DateTimeField(null=True, blank=True)),
                ('controller', models.TextField(null=True, blank=True)),
                ('status', models.TextField(null=True, blank=True)),
                ('connection', models.CharField(max_length=3, null=True, blank=True)),
                ('number_of_data', models.IntegerField(null=True, blank=True)),
                ('readout_interval', models.IntegerField(null=True, blank=True)),
                ('address1', models.TextField(null=True, blank=True)),
                ('address2', models.TextField(null=True, blank=True)),
                ('alarm_status', models.TextField(null=True, blank=True)),
                ('alarm_low1', models.FloatField(null=True, blank=True)),
                ('alarm_low2', models.FloatField(null=True, blank=True)),
                ('alarm_high1', models.FloatField(null=True, blank=True)),
                ('alarm_high2', models.FloatField(null=True, blank=True)),
            ],
            options={
                'db_table': 'config_history',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DataCryocon',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('datetime', models.DateTimeField(null=True, blank=True)),
                ('data', models.TextField(null=True, blank=True)),
                ('status', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'data_cryocon',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DataPressurecontroller',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('datetime', models.DateTimeField(null=True, blank=True)),
                ('data', models.TextField(null=True, blank=True)),
                ('status', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'data_pressurecontroller',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DataTestdev',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('datetime', models.DateTimeField(null=True, blank=True)),
                ('data', models.TextField(null=True, blank=True)),
                ('status', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'data_testdev',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DataTestdevice',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('date_time', models.DateTimeField(null=True, blank=True)),
                ('data', models.TextField(null=True, blank=True)),
                ('status', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'data_testdevice',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('datetime', models.DateTimeField(null=True, blank=True)),
                ('data', models.TextField(null=True, blank=True)),
                ('status', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'test',
                'managed': False,
            },
        ),
    ]
