"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import ni_measurementlink_service._internal.stubs.ni.measurementlink.sessionmanagement.v1.session_management_service_pb2 as ni_measurementlink_sessionmanagement_v1_session_management_service_pb2

class SessionManagementServiceStub:
    """Service to keep track of open sessions used by measurement services, and to allow measurement services to access sessions by pin and site."""

    def __init__(self, channel: grpc.Channel) -> None: ...
    ReserveSessions: grpc.UnaryUnaryMultiCallable[
        ni_measurementlink_sessionmanagement_v1_session_management_service_pb2.ReserveSessionsRequest,
        ni_measurementlink_sessionmanagement_v1_session_management_service_pb2.ReserveSessionsResponse,
    ]
    """Reserve session(s) for the given pins or relays, sites, and instrument type ID and returns the information needed to create or access the session.
    (Will be implemented in AB#2046548) Also reserves the session so other processes cannot access it with a ReserveSessions() call.
    Status Codes for errors:
    - INVALID_ARGUMENT:
        - Pin Map Context references a site number that is not defined in the pin map
        - Pin or relay name does not match any pin, pin group, relay, or relay group names in the pin map
        - Timeout specified is less than -1.
    - NOT_FOUND:
        - Pin Map Context has a pin map ID that does not match any pin maps registered with the Pin Map Service.
    - UNAVAILABLE:
        - Session(s) were already reserved and didn't become available before the specified timeout expired.
    """
    UnreserveSessions: grpc.UnaryUnaryMultiCallable[
        ni_measurementlink_sessionmanagement_v1_session_management_service_pb2.UnreserveSessionsRequest,
        ni_measurementlink_sessionmanagement_v1_session_management_service_pb2.UnreserveSessionsResponse,
    ]
    """Unreserves sessions so they can be accessed by other clients.
    - RESOURCE_EXHAUSTED:
        - Error occurred while unreserving sessions.
    """
    RegisterSessions: grpc.UnaryUnaryMultiCallable[
        ni_measurementlink_sessionmanagement_v1_session_management_service_pb2.RegisterSessionsRequest,
        ni_measurementlink_sessionmanagement_v1_session_management_service_pb2.RegisterSessionsResponse,
    ]
    """Registers the sessions with this service. Indicates that the sessions are open and will need to be closed later.
    Status Codes for errors:
    - ALREADY_EXISTS:
        - Session by the same name is already registered.
    - INVALID_ARGUMENT:
        - Session names list has an empty string.
    """
    UnregisterSessions: grpc.UnaryUnaryMultiCallable[
        ni_measurementlink_sessionmanagement_v1_session_management_service_pb2.UnregisterSessionsRequest,
        ni_measurementlink_sessionmanagement_v1_session_management_service_pb2.UnregisterSessionsResponse,
    ]
    """Unregisters the sessions with this service. Indicates that the sessions have been closed and will need to be reopened before they can be used again."""
    ReserveAllRegisteredSessions: grpc.UnaryUnaryMultiCallable[
        ni_measurementlink_sessionmanagement_v1_session_management_service_pb2.ReserveAllRegisteredSessionsRequest,
        ni_measurementlink_sessionmanagement_v1_session_management_service_pb2.ReserveAllRegisteredSessionsResponse,
    ]
    """Reserves and gets all sessions currently registered with this service.
    - INVALID_ARGUMENT:
        - Timeout specified is less than -1.
    - UNAVAILABLE:
        - Session(s) were already reserved and didn't become available before the specified timeout expired.
    """

class SessionManagementServiceServicer(metaclass=abc.ABCMeta):
    """Service to keep track of open sessions used by measurement services, and to allow measurement services to access sessions by pin and site."""

    @abc.abstractmethod
    def ReserveSessions(
        self,
        request: ni_measurementlink_sessionmanagement_v1_session_management_service_pb2.ReserveSessionsRequest,
        context: grpc.ServicerContext,
    ) -> ni_measurementlink_sessionmanagement_v1_session_management_service_pb2.ReserveSessionsResponse:
        """Reserve session(s) for the given pins or relays, sites, and instrument type ID and returns the information needed to create or access the session.
        (Will be implemented in AB#2046548) Also reserves the session so other processes cannot access it with a ReserveSessions() call.
        Status Codes for errors:
        - INVALID_ARGUMENT:
            - Pin Map Context references a site number that is not defined in the pin map
            - Pin or relay name does not match any pin, pin group, relay, or relay group names in the pin map
            - Timeout specified is less than -1.
        - NOT_FOUND:
            - Pin Map Context has a pin map ID that does not match any pin maps registered with the Pin Map Service.
        - UNAVAILABLE:
            - Session(s) were already reserved and didn't become available before the specified timeout expired.
        """
    @abc.abstractmethod
    def UnreserveSessions(
        self,
        request: ni_measurementlink_sessionmanagement_v1_session_management_service_pb2.UnreserveSessionsRequest,
        context: grpc.ServicerContext,
    ) -> ni_measurementlink_sessionmanagement_v1_session_management_service_pb2.UnreserveSessionsResponse:
        """Unreserves sessions so they can be accessed by other clients.
        - RESOURCE_EXHAUSTED:
            - Error occurred while unreserving sessions.
        """
    @abc.abstractmethod
    def RegisterSessions(
        self,
        request: ni_measurementlink_sessionmanagement_v1_session_management_service_pb2.RegisterSessionsRequest,
        context: grpc.ServicerContext,
    ) -> ni_measurementlink_sessionmanagement_v1_session_management_service_pb2.RegisterSessionsResponse:
        """Registers the sessions with this service. Indicates that the sessions are open and will need to be closed later.
        Status Codes for errors:
        - ALREADY_EXISTS:
            - Session by the same name is already registered.
        - INVALID_ARGUMENT:
            - Session names list has an empty string.
        """
    @abc.abstractmethod
    def UnregisterSessions(
        self,
        request: ni_measurementlink_sessionmanagement_v1_session_management_service_pb2.UnregisterSessionsRequest,
        context: grpc.ServicerContext,
    ) -> ni_measurementlink_sessionmanagement_v1_session_management_service_pb2.UnregisterSessionsResponse:
        """Unregisters the sessions with this service. Indicates that the sessions have been closed and will need to be reopened before they can be used again."""
    @abc.abstractmethod
    def ReserveAllRegisteredSessions(
        self,
        request: ni_measurementlink_sessionmanagement_v1_session_management_service_pb2.ReserveAllRegisteredSessionsRequest,
        context: grpc.ServicerContext,
    ) -> ni_measurementlink_sessionmanagement_v1_session_management_service_pb2.ReserveAllRegisteredSessionsResponse:
        """Reserves and gets all sessions currently registered with this service.
        - INVALID_ARGUMENT:
            - Timeout specified is less than -1.
        - UNAVAILABLE:
            - Session(s) were already reserved and didn't become available before the specified timeout expired.
        """

def add_SessionManagementServiceServicer_to_server(servicer: SessionManagementServiceServicer, server: grpc.Server) -> None: ...