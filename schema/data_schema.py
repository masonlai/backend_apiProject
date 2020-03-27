from flask_marshmallow import Marshmallow,fields
from marshmallow import validate,fields

ma = Marshmallow()

class getSchema(ma.Schema):

    orderNo = fields.Str(required=True)

class customerSchema(ma.Schema):

    customer = fields.Str(required=True)

class Schema(ma.Schema):

    orderItemCode = fields.Str(required=True)
    description = fields.Str(required=True)
    quantity = fields.Str(required=True)
    customer = fields.Str(required=True)
    address = fields.Str(required=True)
    date = fields.Date(required=True,format='%d-%m-%Y')
    time = fields.Time(required=True,format='%H:%M')

class checkSchema(ma.Schema):

    orderNo = fields.Str(required=True)
    orderItemCode = fields.Str(required=True)
    description = fields.Str(required=True)
    quantity = fields.Str(required=True)
    customer = fields.Str(required=True)
    address = fields.Str(required=True)
    date = fields.Date(required=True,format='%d-%m-%Y')
    time = fields.Time(required=True,format='%H:%M')

class updateSchema(ma.Schema):

    orderNo = fields.Str(required=True)
    orderItemCode = fields.Str(required=True)
    description = fields.Str(required=True)
    quantity = fields.Str(required=True)
    customer = fields.Str(required=True)
    address = fields.Str(required=True)