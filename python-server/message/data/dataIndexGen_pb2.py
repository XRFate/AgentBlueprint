# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dataIndexGen.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x64\x61taIndexGen.proto\x12\tprotoData\"\\\n\x06\x41\x63tion\x12\x1a\n\x12\x61\x63tion_description\x18\x01 \x01(\t\x12\x10\n\x08\x64uration\x18\x02 \x01(\x05\x12\x12\n\nstart_time\x18\x03 \x01(\x04\x12\x10\n\x08\x65nd_time\x18\x04 \x01(\x04\"-\n\x07\x41\x63tions\x12\"\n\x07\x61\x63tions\x18\x01 \x03(\x0b\x32\x11.protoData.Action\"=\n\tEmojiData\x12\x19\n\x11\x65moji_description\x18\x01 \x01(\t\x12\x15\n\remoji_unicode\x18\x02 \x01(\t\"7\n\x0cParsedAction\x12\'\n\tEmojiList\x18\x01 \x01(\x0b\x32\x14.protoData.EmojiDataB\x17Z\x15golang-client/messageb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dataIndexGen_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\025golang-client/message'
  _globals['_ACTION']._serialized_start=33
  _globals['_ACTION']._serialized_end=125
  _globals['_ACTIONS']._serialized_start=127
  _globals['_ACTIONS']._serialized_end=172
  _globals['_EMOJIDATA']._serialized_start=174
  _globals['_EMOJIDATA']._serialized_end=235
  _globals['_PARSEDACTION']._serialized_start=237
  _globals['_PARSEDACTION']._serialized_end=292
# @@protoc_insertion_point(module_scope)