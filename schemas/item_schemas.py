from marshmallow import Schema, fields, validate


class ItemSchema(Schema):
  name = fields.Str(required=True, validate=[validate.Length(min=1, max=100)])
  count = fields.Int(required=True, validate=[validate.Range(min=1)])
  price = fields.Float(required=True, validate=[validate.Range(min=0.01)])
