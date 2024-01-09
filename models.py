from tortoise import fields
from tortoise.models import Model


class DataModel(Model):
    id = fields.IntField(pk=True)
    sourceCountry = fields.CharField(max_length=255)
    destinationCountry = fields.CharField(max_length=255)
    millisecond = fields.IntField()
    type = fields.CharField(max_length=255)
    weight = fields.IntField()
    attackTime = fields.CharField(max_length=255)
