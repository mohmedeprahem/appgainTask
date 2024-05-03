from marshmallow import Schema, fields, validate

class RegisterSchema(Schema):
  username = fields.Str(required=True, validate=[validate.Length(min=1, max=100)])
  email = fields.Email(required=True)
  password = fields.Str(required=True, validate=[validate.Length(min=8, max=100)])
