# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='test.proto',
  package='ni.measurements.v1',
  syntax='proto3',
  serialized_options=b'\252\0024NationalInstruments.MeasurementServices.Measurements',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\ntest.proto\x12\x12ni.measurements.v1\"\xd4\x01\n\x14MeasurementParameter\x12\x12\n\nfloat_data\x18\x01 \x01(\x02\x12\x13\n\x0b\x64ouble_data\x18\x02 \x01(\x01\x12\x12\n\nint32_data\x18\x03 \x01(\x05\x12\x13\n\x0buint32_data\x18\x04 \x01(\r\x12\x12\n\nint64_data\x18\x05 \x01(\x03\x12\x13\n\x0buint64_data\x18\x06 \x01(\x04\x12\x11\n\tbool_data\x18\x07 \x01(\x08\x12\x13\n\x0bstring_data\x18\x08 \x01(\t\x12\x19\n\x11\x64ouble_array_data\x18\t \x03(\x01\x42\x37\xaa\x02\x34NationalInstruments.MeasurementServices.Measurementsb\x06proto3'
)




_MEASUREMENTPARAMETER = _descriptor.Descriptor(
  name='MeasurementParameter',
  full_name='ni.measurements.v1.MeasurementParameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='float_data', full_name='ni.measurements.v1.MeasurementParameter.float_data', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='double_data', full_name='ni.measurements.v1.MeasurementParameter.double_data', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='int32_data', full_name='ni.measurements.v1.MeasurementParameter.int32_data', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uint32_data', full_name='ni.measurements.v1.MeasurementParameter.uint32_data', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='int64_data', full_name='ni.measurements.v1.MeasurementParameter.int64_data', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uint64_data', full_name='ni.measurements.v1.MeasurementParameter.uint64_data', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bool_data', full_name='ni.measurements.v1.MeasurementParameter.bool_data', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='string_data', full_name='ni.measurements.v1.MeasurementParameter.string_data', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='double_array_data', full_name='ni.measurements.v1.MeasurementParameter.double_array_data', index=8,
      number=9, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=247,
)

DESCRIPTOR.message_types_by_name['MeasurementParameter'] = _MEASUREMENTPARAMETER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MeasurementParameter = _reflection.GeneratedProtocolMessageType('MeasurementParameter', (_message.Message,), {
  'DESCRIPTOR' : _MEASUREMENTPARAMETER,
  '__module__' : 'test_pb2'
  # @@protoc_insertion_point(class_scope:ni.measurements.v1.MeasurementParameter)
  })
_sym_db.RegisterMessage(MeasurementParameter)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)