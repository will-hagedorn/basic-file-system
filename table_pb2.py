# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: table.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'table.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0btable.proto\"+\n\tColSumReq\x12\x0e\n\x06\x63olumn\x18\x01 \x01(\t\x12\x0e\n\x06\x66ormat\x18\x02 \x01(\t\"*\n\nColSumResp\x12\r\n\x05\x65rror\x18\x01 \x01(\t\x12\r\n\x05total\x18\x02 \x01(\x03\"\x1d\n\tUploadReq\x12\x10\n\x08\x63sv_data\x18\x01 \x01(\t\"\x1b\n\nUploadResp\x12\r\n\x05\x65rror\x18\x01 \x01(\t2M\n\x05Table\x12!\n\x06\x43olSum\x12\n.ColSumReq\x1a\x0b.ColSumResp\x12!\n\x06Upload\x12\n.UploadReq\x1a\x0b.UploadRespb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'table_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_COLSUMREQ']._serialized_start=15
  _globals['_COLSUMREQ']._serialized_end=58
  _globals['_COLSUMRESP']._serialized_start=60
  _globals['_COLSUMRESP']._serialized_end=102
  _globals['_UPLOADREQ']._serialized_start=104
  _globals['_UPLOADREQ']._serialized_end=133
  _globals['_UPLOADRESP']._serialized_start=135
  _globals['_UPLOADRESP']._serialized_end=162
  _globals['_TABLE']._serialized_start=164
  _globals['_TABLE']._serialized_end=241
# @@protoc_insertion_point(module_scope)
