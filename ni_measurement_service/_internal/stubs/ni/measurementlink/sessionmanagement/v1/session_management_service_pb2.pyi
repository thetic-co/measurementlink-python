"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import ni.measurementlink.pin_map_context_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Session(google.protobuf.message.Message):
    """Session identification information. Used to reference a specific session in NI grpc-device or in any other driver session management system."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Required. Session name to uniquely identify the session in NI grpc-device or other drivers."""
    def __init__(
        self,
        *,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name"]) -> None: ...

global___Session = Session

class SessionInformation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SESSION_FIELD_NUMBER: builtins.int
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    CHANNEL_LIST_FIELD_NUMBER: builtins.int
    INSTRUMENT_TYPE_ID_FIELD_NUMBER: builtins.int
    SESSION_EXISTS_FIELD_NUMBER: builtins.int
    @property
    def session(self) -> global___Session:
        """Session identifier used to identify the session in the session management service, as well as in driver services such as grpc-device.
        This field is readonly.
        """
    resource_name: builtins.str
    """Resource name used to open this session in the driver.
    This field is readonly.
    """
    channel_list: builtins.str
    """Channel list used for driver initialization and measurement methods.
    This field is empty for any SessionInformation returned from ReserveAllRegisteredSessions.
    This field is readonly.
    """
    instrument_type_id: builtins.str
    """Instrument type ID to identify which type of instrument the session represents.
    Pin maps have built in instrument definitions using the following NI driver based instrument type ids:
         "niDCPower"
         "niDigitalPattern"
         "niScope"
         "niDMM"
         "niDAQmx".
    For custom instruments the user defined instrument type id is defined in the pin map file.
    This field is readonly.
    """
    session_exists: builtins.bool
    """Indicates whether the session exists in the Session Manager. This indicates whether the session has been created.
    This field is readonly.
    """
    def __init__(
        self,
        *,
        session: global___Session | None = ...,
        resource_name: builtins.str = ...,
        channel_list: builtins.str = ...,
        instrument_type_id: builtins.str = ...,
        session_exists: builtins.bool = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["session", b"session"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "channel_list",
            b"channel_list",
            "instrument_type_id",
            b"instrument_type_id",
            "resource_name",
            b"resource_name",
            "session",
            b"session",
            "session_exists",
            b"session_exists",
        ],
    ) -> None: ...

global___SessionInformation = SessionInformation

class ReserveSessionsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PIN_MAP_CONTEXT_FIELD_NUMBER: builtins.int
    PIN_NAMES_FIELD_NUMBER: builtins.int
    INSTRUMENT_TYPE_ID_FIELD_NUMBER: builtins.int
    TIMEOUT_IN_MILLISECONDS_FIELD_NUMBER: builtins.int
    @property
    def pin_map_context(self) -> ni.measurementlink.pin_map_context_pb2.PinMapContext:
        """Required. Includes the pin map ID for the pin map in the Pin Map Service, as well as the list of sites for the measurement."""
    @property
    def pin_names(
        self,
    ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Optional. List of pin names or pin group names to use for the measurement. If unspecified, reserve sessions for all pins in the registered pin map resource."""
    instrument_type_id: builtins.str
    """Optional. Instrument type ID for the measurement. If unspecified, reserve sessions for all instrument types connected in the registered pin map resource.
    Pin maps have built in instrument definitions using the following NI driver based instrument type ids:
         "niDCPower"
         "niDigitalPattern"
         "niScope"
         "niDMM"
         "niDAQmx".
    For custom instruments the user defined instrument type id is defined in the pin map file.
    """
    timeout_in_milliseconds: builtins.int
    """Optional. Timeout for the reservation request.
    Allowed values: 0 (non-blocking, fails immediately if resources cannot be reserved), -1 (infinite timeout), or any other positive numeric value (wait for that number of milliseconds)
    """
    def __init__(
        self,
        *,
        pin_map_context: ni.measurementlink.pin_map_context_pb2.PinMapContext | None = ...,
        pin_names: collections.abc.Iterable[builtins.str] | None = ...,
        instrument_type_id: builtins.str = ...,
        timeout_in_milliseconds: builtins.int = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["pin_map_context", b"pin_map_context"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "instrument_type_id",
            b"instrument_type_id",
            "pin_map_context",
            b"pin_map_context",
            "pin_names",
            b"pin_names",
            "timeout_in_milliseconds",
            b"timeout_in_milliseconds",
        ],
    ) -> None: ...

global___ReserveSessionsRequest = ReserveSessionsRequest

class ReserveSessionsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SESSIONS_FIELD_NUMBER: builtins.int
    @property
    def sessions(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___SessionInformation
    ]:
        """List of information needed to create or use each session for the given pin, site, and instrument type ID.
        This field is readonly.
        """
    def __init__(
        self,
        *,
        sessions: collections.abc.Iterable[global___SessionInformation] | None = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["sessions", b"sessions"]
    ) -> None: ...

global___ReserveSessionsResponse = ReserveSessionsResponse

class UnreserveSessionsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SESSIONS_FIELD_NUMBER: builtins.int
    @property
    def sessions(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___SessionInformation
    ]:
        """Required. List of information of sessions to be unreserved in the session management service."""
    def __init__(
        self,
        *,
        sessions: collections.abc.Iterable[global___SessionInformation] | None = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["sessions", b"sessions"]
    ) -> None: ...

global___UnreserveSessionsRequest = UnreserveSessionsRequest

class UnreserveSessionsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___UnreserveSessionsResponse = UnreserveSessionsResponse

class RegisterSessionsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SESSIONS_FIELD_NUMBER: builtins.int
    @property
    def sessions(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___SessionInformation
    ]:
        """Required. List of sessions to register with the session management service to track as the sessions are open."""
    def __init__(
        self,
        *,
        sessions: collections.abc.Iterable[global___SessionInformation] | None = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["sessions", b"sessions"]
    ) -> None: ...

global___RegisterSessionsRequest = RegisterSessionsRequest

class RegisterSessionsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___RegisterSessionsResponse = RegisterSessionsResponse

class UnregisterSessionsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SESSIONS_FIELD_NUMBER: builtins.int
    @property
    def sessions(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___SessionInformation
    ]:
        """Required. List of sessions to unregister with the session management service to mark them as sessions were closed."""
    def __init__(
        self,
        *,
        sessions: collections.abc.Iterable[global___SessionInformation] | None = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["sessions", b"sessions"]
    ) -> None: ...

global___UnregisterSessionsRequest = UnregisterSessionsRequest

class UnregisterSessionsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___UnregisterSessionsResponse = UnregisterSessionsResponse

class ReserveAllRegisteredSessionsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TIMEOUT_IN_MILLISECONDS_FIELD_NUMBER: builtins.int
    timeout_in_milliseconds: builtins.int
    """Optional. Timeout for the reservation request.
    Allowed values: 0 (non-blocking, fails immediately if resources cannot be reserved), -1 (infinite timeout), or any other positive numeric value (wait for that number of milliseconds)
    """
    def __init__(
        self,
        *,
        timeout_in_milliseconds: builtins.int = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "timeout_in_milliseconds", b"timeout_in_milliseconds"
        ],
    ) -> None: ...

global___ReserveAllRegisteredSessionsRequest = ReserveAllRegisteredSessionsRequest

class ReserveAllRegisteredSessionsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SESSIONS_FIELD_NUMBER: builtins.int
    @property
    def sessions(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___SessionInformation
    ]:
        """Sessions currently registered in the session management service."""
    def __init__(
        self,
        *,
        sessions: collections.abc.Iterable[global___SessionInformation] | None = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["sessions", b"sessions"]
    ) -> None: ...

global___ReserveAllRegisteredSessionsResponse = ReserveAllRegisteredSessionsResponse