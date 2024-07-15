# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ni/measurementlink/discovery/v1/discovery_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7ni/measurementlink/discovery/v1/discovery_service.proto\x12\x1fni.measurementlink.discovery.v1\"\x84\x02\n\x11ServiceDescriptor\x12\x14\n\x0c\x64isplay_name\x18\x01 \x01(\t\x12\x17\n\x0f\x64\x65scription_url\x18\x02 \x01(\t\x12\x1b\n\x13provided_interfaces\x18\x03 \x03(\t\x12\x15\n\rservice_class\x18\x04 \x01(\t\x12X\n\x0b\x61nnotations\x18\x05 \x03(\x0b\x32\x43.ni.measurementlink.discovery.v1.ServiceDescriptor.AnnotationsEntry\x1a\x32\n\x10\x41nnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"Z\n\x0fServiceLocation\x12\x10\n\x08location\x18\x01 \x01(\t\x12\x15\n\rinsecure_port\x18\x02 \x01(\t\x12\x1e\n\x16ssl_authenticated_port\x18\x03 \x01(\t\"\xad\x01\n\x16RegisterServiceRequest\x12O\n\x13service_description\x18\x01 \x01(\x0b\x32\x32.ni.measurementlink.discovery.v1.ServiceDescriptor\x12\x42\n\x08location\x18\x02 \x01(\x0b\x32\x30.ni.measurementlink.discovery.v1.ServiceLocation\"2\n\x17RegisterServiceResponse\x12\x17\n\x0fregistration_id\x18\x01 \x01(\t\"3\n\x18UnregisterServiceRequest\x12\x17\n\x0fregistration_id\x18\x01 \x01(\t\"\x1b\n\x19UnregisterServiceResponse\"6\n\x18\x45numerateServicesRequest\x12\x1a\n\x12provided_interface\x18\x01 \x01(\t\"\x80\x01\n\x19\x45numerateServicesResponse\x12N\n\x12\x61vailable_services\x18\x01 \x03(\x0b\x32\x32.ni.measurementlink.discovery.v1.ServiceDescriptor\x12\x13\n\x0bunreachable\x18\x02 \x03(\t\"e\n\x15ResolveServiceRequest\x12\x1a\n\x12provided_interface\x18\x01 \x01(\t\x12\x15\n\rservice_class\x18\x02 \x01(\t\x12\x19\n\x11\x64\x65ployment_target\x18\x03 \x01(\t\"6\n\x15\x43omputeNodeDescriptor\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x10\n\x08is_local\x18\x02 \x01(\x08\"\x1e\n\x1c\x45numerateComputeNodesRequest\"n\n\x1d\x45numerateComputeNodesResponse\x12M\n\rcompute_nodes\x18\x01 \x03(\x0b\x32\x36.ni.measurementlink.discovery.v1.ComputeNodeDescriptor2\xc8\x05\n\x10\x44iscoveryService\x12\x84\x01\n\x0fRegisterService\x12\x37.ni.measurementlink.discovery.v1.RegisterServiceRequest\x1a\x38.ni.measurementlink.discovery.v1.RegisterServiceResponse\x12\x8a\x01\n\x11UnregisterService\x12\x39.ni.measurementlink.discovery.v1.UnregisterServiceRequest\x1a:.ni.measurementlink.discovery.v1.UnregisterServiceResponse\x12\x8a\x01\n\x11\x45numerateServices\x12\x39.ni.measurementlink.discovery.v1.EnumerateServicesRequest\x1a:.ni.measurementlink.discovery.v1.EnumerateServicesResponse\x12z\n\x0eResolveService\x12\x36.ni.measurementlink.discovery.v1.ResolveServiceRequest\x1a\x30.ni.measurementlink.discovery.v1.ServiceLocation\x12\x96\x01\n\x15\x45numerateComputeNodes\x12=.ni.measurementlink.discovery.v1.EnumerateComputeNodesRequest\x1a>.ni.measurementlink.discovery.v1.EnumerateComputeNodesResponseB\xcc\x01\n#com.ni.measurementlink.discovery.v1B\x15\x44iscoveryServiceProtoP\x01Z\x0b\x64iscoveryv1\xa2\x02\x04NIMD\xaa\x02\x30NationalInstruments.MeasurementLink.Discovery.V1\xca\x02\x1fNI\\MeasurementLink\\Discovery\\V1\xea\x02\"NI::MeasurementLink::Discovery::V1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ni.measurementlink.discovery.v1.discovery_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n#com.ni.measurementlink.discovery.v1B\025DiscoveryServiceProtoP\001Z\013discoveryv1\242\002\004NIMD\252\0020NationalInstruments.MeasurementLink.Discovery.V1\312\002\037NI\\MeasurementLink\\Discovery\\V1\352\002\"NI::MeasurementLink::Discovery::V1'
  _SERVICEDESCRIPTOR_ANNOTATIONSENTRY._options = None
  _SERVICEDESCRIPTOR_ANNOTATIONSENTRY._serialized_options = b'8\001'
  _SERVICEDESCRIPTOR._serialized_start=93
  _SERVICEDESCRIPTOR._serialized_end=353
  _SERVICEDESCRIPTOR_ANNOTATIONSENTRY._serialized_start=303
  _SERVICEDESCRIPTOR_ANNOTATIONSENTRY._serialized_end=353
  _SERVICELOCATION._serialized_start=355
  _SERVICELOCATION._serialized_end=445
  _REGISTERSERVICEREQUEST._serialized_start=448
  _REGISTERSERVICEREQUEST._serialized_end=621
  _REGISTERSERVICERESPONSE._serialized_start=623
  _REGISTERSERVICERESPONSE._serialized_end=673
  _UNREGISTERSERVICEREQUEST._serialized_start=675
  _UNREGISTERSERVICEREQUEST._serialized_end=726
  _UNREGISTERSERVICERESPONSE._serialized_start=728
  _UNREGISTERSERVICERESPONSE._serialized_end=755
  _ENUMERATESERVICESREQUEST._serialized_start=757
  _ENUMERATESERVICESREQUEST._serialized_end=811
  _ENUMERATESERVICESRESPONSE._serialized_start=814
  _ENUMERATESERVICESRESPONSE._serialized_end=942
  _RESOLVESERVICEREQUEST._serialized_start=944
  _RESOLVESERVICEREQUEST._serialized_end=1045
  _COMPUTENODEDESCRIPTOR._serialized_start=1047
  _COMPUTENODEDESCRIPTOR._serialized_end=1101
  _ENUMERATECOMPUTENODESREQUEST._serialized_start=1103
  _ENUMERATECOMPUTENODESREQUEST._serialized_end=1133
  _ENUMERATECOMPUTENODESRESPONSE._serialized_start=1135
  _ENUMERATECOMPUTENODESRESPONSE._serialized_end=1245
  _DISCOVERYSERVICE._serialized_start=1248
  _DISCOVERYSERVICE._serialized_end=1960
# @@protoc_insertion_point(module_scope)