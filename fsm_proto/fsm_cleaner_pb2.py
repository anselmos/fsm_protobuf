# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: fsm_proto/fsm_cleaner.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'fsm_proto/fsm_cleaner.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x66sm_proto/fsm_cleaner.proto\"1\n\x11RemoveFileRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0e\n\x06md5sum\x18\x02 \x01(\t\"4\n\x12RemoveFileResponse\x12\x0f\n\x07removed\x18\x01 \x01(\x08\x12\r\n\x05\x65rror\x18\x02 \x01(\x08\x32\x45\n\nFSMCleaner\x12\x37\n\nRemoveFile\x12\x12.RemoveFileRequest\x1a\x13.RemoveFileResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'fsm_proto.fsm_cleaner_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_REMOVEFILEREQUEST']._serialized_start=31
  _globals['_REMOVEFILEREQUEST']._serialized_end=80
  _globals['_REMOVEFILERESPONSE']._serialized_start=82
  _globals['_REMOVEFILERESPONSE']._serialized_end=134
  _globals['_FSMCLEANER']._serialized_start=136
  _globals['_FSMCLEANER']._serialized_end=205
# @@protoc_insertion_point(module_scope)