from __future__ import unicode_literals
from django.db import models
from djangotoolbox import fields


class Controller(models.Model):
    name                = models.TextField()
    status              = models.TextField()
    alarm_status        = fields.ListField(models.TextField())
    warning_low         = fields.ListField(models.FloatField())
    warning_high        = fields.ListField(models.FloatField())
    alarm_low           = fields.ListField(models.FloatField())
    alarm_high          = fields.ListField(models.FloatField())
    readout_interval    = models.IntegerField()
    alarm_recurrence    = fields.ListField(models.FloatField())
    description         = fields.ListField(models.TextField())
    number_of_data      = models.IntegerField()
    additional_params   = fields.DictField()

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Controller._meta.fields]

    class MongoMeta:
        managed = False
        db_table = 'controllers'

def getDataModel(db_table_name):
    class Here(models.Model):
        when = models.DateTimeField()
        data = fields.ListField(models.FloatField())
        status = fields.ListField(models.IntegerField())
        class MongoMeta:
            indexes = [('when',1)]
            managed = False
            db_table = db_table_name

    return Here

