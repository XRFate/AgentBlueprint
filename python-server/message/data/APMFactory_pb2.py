# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: APMFactory.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x41PMFactory.proto\x12\tprotoData\"\x96\x01\n\rNodeConnector\x12=\n\x0binput_nodes\x18\x01 \x03(\x0b\x32(.protoData.NodeConnector.InputNodesEntry\x1a\x46\n\x0fInputNodesEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\"\n\x05value\x18\x02 \x01(\x0b\x32\x13.protoData.NodeData:\x02\x38\x01\"\xb0\x01\n\x08NodeData\x12\x0f\n\x07node_id\x18\x01 \x01(\x04\x12\x36\n\x0e\x66unction_param\x18\x02 \x01(\x0b\x32\x19.protoData.FunctionParamsH\x00\x88\x01\x01\x12\x35\n\x0enode_structure\x18\x03 \x01(\x0b\x32\x18.protoData.NodeConnectorH\x01\x88\x01\x01\x42\x11\n\x0f_function_paramB\x11\n\x0f_node_structure\"Y\n\x08\x46ileTree\x12\x11\n\ttree_type\x18\x01 \x01(\x05\x12&\n\troot_node\x18\x02 \x01(\x0b\x32\x13.protoData.NodeData\x12\x12\n\nis_default\x18\x03 \x01(\x08\"S\n\x07\x61pmFile\x12\"\n\x05trees\x18\x01 \x03(\x0b\x32\x13.protoData.FileTree\x12\x0e\n\x06usr_id\x18\x02 \x01(\x05\x12\x14\n\x0c\x63haracter_id\x18\x03 \x01(\x05\"\xc8\x01\n\x0e\x46unctionParams\x12\x1c\n\x0f\x66unction_prompt\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1b\n\x0einput_data_obj\x18\x02 \x01(\x0cH\x01\x88\x01\x01\x12\x17\n\ninput_text\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x1a\n\rsystem_prompt\x18\x04 \x01(\tH\x03\x88\x01\x01\x42\x12\n\x10_function_promptB\x11\n\x0f_input_data_objB\r\n\x0b_input_textB\x10\n\x0e_system_promptB\x17Z\x15golang-client/messageb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'APMFactory_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\025golang-client/message'
  _globals['_NODECONNECTOR_INPUTNODESENTRY']._loaded_options = None
  _globals['_NODECONNECTOR_INPUTNODESENTRY']._serialized_options = b'8\001'
  _globals['_NODECONNECTOR']._serialized_start=32
  _globals['_NODECONNECTOR']._serialized_end=182
  _globals['_NODECONNECTOR_INPUTNODESENTRY']._serialized_start=112
  _globals['_NODECONNECTOR_INPUTNODESENTRY']._serialized_end=182
  _globals['_NODEDATA']._serialized_start=185
  _globals['_NODEDATA']._serialized_end=361
  _globals['_FILETREE']._serialized_start=363
  _globals['_FILETREE']._serialized_end=452
  _globals['_APMFILE']._serialized_start=454
  _globals['_APMFILE']._serialized_end=537
  _globals['_FUNCTIONPARAMS']._serialized_start=540
  _globals['_FUNCTIONPARAMS']._serialized_end=740
# @@protoc_insertion_point(module_scope)
