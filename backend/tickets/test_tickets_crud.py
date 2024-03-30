import pytest
from rest_framework.test import APIClient
from rest_framework import status
from .models import Ticket
from events.models import Event
from accounts.models import Account

account_data = {
    "email": "test@email.com",
    "password": "testpassword",
    "first_name": "test",
    "last_name": "account",
    "phone_number": "1234567890",
    "address": "test address",
}

event_data = {
    "title": "test event",
    "description": "test description",
    "organizer": "test organizer",
    "date": "2021-01-01",
    "time": "00:00:00",
    "event_type": "virtual",
    "location": "test location",
    "ticket_price": 0.0,
}

ticket_data = {
    "event": 1,
    "buyer": 1,
    "response": "{}",
    "purchase_date": "2021-01-01",
    "status": "pending",
    "price": 100
}

@pytest.fixture
def test_user():
    user = Account.objects.create(**account_data)
    return user


@pytest.fixture
def test_event(test_user):
    event_data_copy = event_data.copy()
    event_data_copy['organizer'] = test_user
    event = Event.objects.create(**event_data_copy)
    return event


@pytest.fixture
def authenticated_client(test_user):
    client = APIClient()
    client.force_authenticate(user=test_user)
    return client


@pytest.mark.django_db
def testTicketCreation_byUnauthenticatedUser_shouldThrowUnauthorized(test_user, test_event):
    # Arrange
    unauthenticated_client = APIClient()
    ticket_data_copy = ticket_data.copy()
    ticket_data_copy['event'] = test_event.id
    ticket_data_copy['buyer'] = test_user.id

    # Act
    response = unauthenticated_client.post("/api/tickets/", ticket_data);

    # Assert
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert Ticket.objects.count() == 0


@pytest.mark.django_db
def testTicketCreation_byAuthenticatedUser_withValidDetails_shouldCreateTicket(authenticated_client, test_event, test_user):
    # Arrange
    ticket_data_copy = ticket_data.copy() 
    ticket_data_copy['event'] = test_event.id
    ticket_data_copy['buyer'] = test_user.id

    # Act
    response = authenticated_client.post("/api/tickets/", ticket_data_copy)

    # Assert
    assert response.status_code == status.HTTP_201_CREATED
    assert Ticket.objects.count() == 1
    assert Ticket.objects.get().event == test_event
    assert Ticket.objects.get().buyer == test_user
    assert Ticket.objects.get().status == 'pending'


@pytest.mark.django_db
def testTicketCreation_byAuthenticatedUser_withInvalidEventId_shouldThrowBadRequest(authenticated_client, test_user):
    # Arrange
    ticket_data_copy = ticket_data.copy()
    ticket_data_copy['event'] = 1
    ticket_data_copy['buyer'] = test_user.id

    # Act
    response = authenticated_client.post("/api/tickets/", ticket_data_copy)

    # Assert
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert Ticket.objects.count() == 0


@pytest.mark.django_db
def testTicketCreation_byAuthenticatedUser_whenBuyerNotEqualsRequestUser_shouldThrowBadRequest(authenticated_client, test_event):
    # Arrange
    ticket_data_copy = ticket_data.copy()
    ticket_data_copy['event'] = test_event.id
    ticket_data_copy['buyer'] = 2

    # Act
    response = authenticated_client.post("/api/tickets/", ticket_data_copy)

    # Assert
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert Ticket.objects.count() == 0


@pytest.mark.django_db
def testListTicket_byUnauthenticatedUser_shouldThrowUnauthorized():
    # Arrange
    unauthenticated_client = APIClient()

    # Act
    response = unauthenticated_client.get("/api/tickets/")

    # Assert
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def testListTicket_byAuthenticatedUser_listsOnlyUsersTickets(authenticated_client, test_user, test_event):
    # Arrange
    ticket_data_copy = ticket_data.copy()
    ticket_data_copy['event'] = test_event
    ticket_data_copy['buyer'] = test_user

    account_data_copy = account_data.copy()
    account_data_copy['email'] = 'test@test.test'
    test_user2 = Account.objects.create(**account_data_copy)

    ticket_data_copy2 = ticket_data.copy()
    ticket_data_copy2['event'] = test_event
    ticket_data_copy2['buyer'] = test_user2

    Ticket.objects.create(**ticket_data_copy)
    Ticket.objects.create(**ticket_data_copy2)

    # Act
    response = authenticated_client.get("/api/tickets/")

    # Assert
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['buyer'] == test_user.id


@pytest.mark.django_db
def testRetrieveTicket_byTicketOwner_shouldReturnSuccessfully(authenticated_client, test_user, test_event):
    # Arrange
    ticket_data_copy = ticket_data.copy()
    ticket_data_copy['event'] = test_event
    ticket_data_copy['buyer'] = test_user

    ticket = Ticket.objects.create(**ticket_data_copy)

    # Act
    response = authenticated_client.get(f"/api/tickets/{ticket.id}/")

    # Assert
    assert response.status_code == status.HTTP_200_OK
    assert response.data['id'] == ticket.id


@pytest.mark.django_db
def testRetrieveTicket_notByTicketOwner_shouldThrowForbidden(authenticated_client, test_user, test_event):
    # Arrange
    account_data_copy = account_data.copy()
    account_data_copy['email'] = 'test@test.com'
    test_user2 = Account.objects.create(**account_data_copy)

    ticket_data_copy = ticket_data.copy()
    ticket_data_copy['event'] = test_event
    ticket_data_copy['buyer'] = test_user2

    ticket = Ticket.objects.create(**ticket_data_copy)

    # Act
    response = authenticated_client.get(f"/api/tickets/{ticket.id}/")

    # Assert
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def testRetrieveTicket_byUnauthenticatedUser_shouldThrowUnauthorized():
    # Arrange
    unauthenticated_client = APIClient()

    # Act
    response = unauthenticated_client.get("/api/tickets/1/")

    # Assert
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
