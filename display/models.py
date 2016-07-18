# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals
from django.db import models
import dbarray


import datetime
from django.core.serializers.json import DjangoJSONEncoder
import decimal
from django.utils.timezone import is_aware


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Config(models.Model):
    controller = models.TextField(blank=True, null=False, primary_key=True)
    status = models.TextField(blank=True, null=True)
    alarm_status = models.TextField(blank=True, null=True)
    warning_low = models.FloatField(blank=True, null=True)
    warning_high = models.FloatField(blank=True, null=True)
    alarm_low = models.FloatField(blank=True, null=True)
    alarm_high = models.FloatField(blank=True, null=True)
    readout_interval = models.IntegerField(blank=True, null=True)
    alarm_recurrence = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    number_of_data = models.IntegerField(blank=True, null=True)
    addresses = models.TextField(blank=True, null=True)
    additional_parameters = models.TextField(blank=True, null=True)


    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Config._meta.fields]

    class Meta:
        managed = False
        db_table = 'config'


class ConfigHistory(models.Model):
    datetime = models.DateTimeField(blank=True, null=False, primary_key=True)
    controller = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    alarm_status = models.TextField(blank=True, null=True)
    warning_low = models.FloatField(blank=True, null=True)
    warning_high = models.FloatField(blank=True, null=True)
    alarm_low = models.FloatField(blank=True, null=True)
    alarm_high = models.FloatField(blank=True, null=True)
    readout_interval = models.IntegerField(blank=True, null=True)
    alarm_recurrence = models.IntegerField(blank=True, null=True)
    description = dbarray.TextArrayField()
    number_of_data = models.IntegerField(blank=True, null=True)
    addresses = models.TextField(blank=True, null=True)
    additional_parameters = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'config_history'


def getModel(db_table_var):
    class MyClass(models.Model):
        datetime = models.DateTimeField(blank=True, null=False, primary_key=True)
        #data = models.FloatField(blank=True, null=True)  # This field type is a guess.
        data = dbarray.FloatArrayField()
        status = models.TextField(blank=True, null=True)  # This field type is a guess.
        class Meta:
            managed = False
            #db_table = 'data_pressurecontroller'
            db_table = db_table_var
    return MyClass

class DataSelection(models.Model):
    controller = models.TextField(blank=True, null=True)
    data_field = models.TextField(blank=True, null=False, primary_key=True)


class DataCryocon(models.Model):
    datetime = models.DateTimeField(blank=True, null=False, primary_key=True)
    data = models.FloatField(blank=True, null=True)  # This field type is a guess.
    status = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'data_cryocon'


class DataPressurecontroller(models.Model):
    datetime = models.DateTimeField(blank=True, null=False, primary_key=True)
    data = models.FloatField(blank=True, null=True)  # This field type is a guess.
    status = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'data_pressurecontroller'


class DataTestdev(models.Model):
    datetime = models.DateTimeField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)  # This field type is a guess.
    status = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'data_testdev'


class DataTestdevice(models.Model):
    date_time = models.DateTimeField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)  # This field type is a guess.
    status = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'data_testdevice'



class Test(models.Model):
    datetime = models.DateTimeField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)  # This field type is a guess.
    status = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'test'
