# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: image_streaming.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='image_streaming.proto',
  package='imagestreaming',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15image_streaming.proto\x12\x0eimagestreaming\"I\n\nImgRequest\x12\x0b\n\x03img\x18\x01 \x01(\x0c\x12\r\n\x05width\x18\x02 \x01(\x05\x12\x0e\n\x06height\x18\x03 \x01(\x05\x12\x0f\n\x07\x63hannel\x18\x04 \x01(\x05\"\x1d\n\x0bImgResponse\x12\x0e\n\x06\x63ounts\x18\x01 \x01(\x05\x32]\n\x0eImageStreaming\x12K\n\nVideoStart\x12\x1a.imagestreaming.ImgRequest\x1a\x1b.imagestreaming.ImgResponse\"\x00(\x01\x30\x01\x62\x06proto3'
)




_IMGREQUEST = _descriptor.Descriptor(
  name='ImgRequest',
  full_name='imagestreaming.ImgRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='img', full_name='imagestreaming.ImgRequest.img', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='width', full_name='imagestreaming.ImgRequest.width', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height', full_name='imagestreaming.ImgRequest.height', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='channel', full_name='imagestreaming.ImgRequest.channel', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=41,
  serialized_end=114,
)


_IMGRESPONSE = _descriptor.Descriptor(
  name='ImgResponse',
  full_name='imagestreaming.ImgResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='counts', full_name='imagestreaming.ImgResponse.counts', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=116,
  serialized_end=145,
)

DESCRIPTOR.message_types_by_name['ImgRequest'] = _IMGREQUEST
DESCRIPTOR.message_types_by_name['ImgResponse'] = _IMGRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ImgRequest = _reflection.GeneratedProtocolMessageType('ImgRequest', (_message.Message,), {
  'DESCRIPTOR' : _IMGREQUEST,
  '__module__' : 'image_streaming_pb2'
  # @@protoc_insertion_point(class_scope:imagestreaming.ImgRequest)
  })
_sym_db.RegisterMessage(ImgRequest)

ImgResponse = _reflection.GeneratedProtocolMessageType('ImgResponse', (_message.Message,), {
  'DESCRIPTOR' : _IMGRESPONSE,
  '__module__' : 'image_streaming_pb2'
  # @@protoc_insertion_point(class_scope:imagestreaming.ImgResponse)
  })
_sym_db.RegisterMessage(ImgResponse)



_IMAGESTREAMING = _descriptor.ServiceDescriptor(
  name='ImageStreaming',
  full_name='imagestreaming.ImageStreaming',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=147,
  serialized_end=240,
  methods=[
  _descriptor.MethodDescriptor(
    name='VideoStart',
    full_name='imagestreaming.ImageStreaming.VideoStart',
    index=0,
    containing_service=None,
    input_type=_IMGREQUEST,
    output_type=_IMGRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_IMAGESTREAMING)

DESCRIPTOR.services_by_name['ImageStreaming'] = _IMAGESTREAMING

# @@protoc_insertion_point(module_scope)