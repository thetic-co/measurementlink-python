"""Test fixtures for unit tests."""

from typing import Generator, cast
from unittest.mock import Mock

import grpc
import pytest
from pytest_mock import MockerFixture

from ni_measurementlink_service._channelpool import GrpcChannelPool
from ni_measurementlink_service._internal import grpc_servicer
from ni_measurementlink_service._internal.discovery_client import DiscoveryClient
from ni_measurementlink_service._internal.grpc_servicer import MeasurementServiceContext
from ni_measurementlink_service.measurement.service import MeasurementService
from ni_measurementlink_service.session_management import (
    MultiSessionReservation,
    SessionManagementClient,
    SingleSessionReservation,
)


@pytest.fixture
def discovery_client(mocker: MockerFixture) -> Mock:
    """Test fixture that creates a mock DiscoveryClient."""
    return mocker.create_autospec(DiscoveryClient)


@pytest.fixture
def grpc_channel(mocker: MockerFixture) -> Mock:
    """Test fixture that creates a mock grpc.Channel."""
    return mocker.create_autospec(grpc.Channel)


@pytest.fixture
def grpc_channel_pool(mocker: MockerFixture) -> Mock:
    """Test fixture that creates a mock GrpcChannelPool."""
    return mocker.create_autospec(GrpcChannelPool)


@pytest.fixture
def measurement_service_context(
    mocker: MockerFixture, measurement_service: Mock
) -> Generator[Mock, None, None]:
    """Test fixture that creates and registers a mock MeasurementServiceContext."""
    mock = mocker.create_autospec(MeasurementServiceContext)
    mock.owner = measurement_service
    token = grpc_servicer.measurement_service_context.set(cast(MeasurementServiceContext, mock))
    try:
        yield mock
    finally:
        grpc_servicer.measurement_service_context.reset(token)


@pytest.fixture
def measurement_service(
    mocker: MockerFixture,
    discovery_client: Mock,
    grpc_channel_pool: Mock,
    session_management_client: Mock,
) -> Mock:
    """Test fixture that creates a mock MeasurementService."""
    mock = mocker.create_autospec(MeasurementService)
    mock.channel_pool = grpc_channel_pool
    mock.discovery_client = discovery_client
    mock.session_management_client = session_management_client
    return mock


@pytest.fixture
def multi_session_reservation(mocker: MockerFixture) -> Mock:
    """Test fixture that creates a mock MultiSessionReservation."""
    return mocker.create_autospec(MultiSessionReservation)


@pytest.fixture
def session_management_client(
    mocker: MockerFixture, multi_session_reservation: Mock, single_session_reservation: Mock
) -> Mock:
    """Test fixture that creates a mock SessionManagementClient."""
    mock = mocker.create_autospec(SessionManagementClient)
    mock.reserve_session.return_value = single_session_reservation
    mock.reserve_sessions.return_value = multi_session_reservation
    mock.reserve_all_registered_sessions.return_value = multi_session_reservation
    return mock


@pytest.fixture
def single_session_reservation(mocker: MockerFixture) -> Mock:
    """Test fixture that creates a mock SingleSessionReservation."""
    return mocker.create_autospec(SingleSessionReservation)