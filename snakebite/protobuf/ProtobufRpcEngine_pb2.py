# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='ProtobufRpcEngine.proto',
  package='hadoop.common',
  serialized_pb=b'\n\x17ProtobufRpcEngine.proto\x12\rhadoop.common\"k\n\x12RequestHeaderProto\x12\x12\n\nmethodName\x18\x01 \x02(\t\x12\"\n\x1a\x64\x65\x63laringClassProtocolName\x18\x02 \x02(\t\x12\x1d\n\x15\x63lientProtocolVersion\x18\x03 \x02(\x04\x42<\n\x1eorg.apache.hadoop.ipc.protobufB\x17ProtobufRpcEngineProtos\xa0\x01\x01')




_REQUESTHEADERPROTO = descriptor.Descriptor(
  name='RequestHeaderProto',
  full_name='hadoop.common.RequestHeaderProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='methodName', full_name='hadoop.common.RequestHeaderProto.methodName', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='declaringClassProtocolName', full_name='hadoop.common.RequestHeaderProto.declaringClassProtocolName', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='clientProtocolVersion', full_name='hadoop.common.RequestHeaderProto.clientProtocolVersion', index=2,
      number=3, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=42,
  serialized_end=149,
)

DESCRIPTOR.message_types_by_name['RequestHeaderProto'] = _REQUESTHEADERPROTO

class RequestHeaderProto(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
  DESCRIPTOR = _REQUESTHEADERPROTO

  # @@protoc_insertion_point(class_scope:hadoop.common.RequestHeaderProto)

# @@protoc_insertion_point(module_scope)
