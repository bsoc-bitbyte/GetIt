import pytest
from rest_framework.test import APIClient
from rest_framework import status
from .models import Event
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
def testEventCreation_withValidDetails_byAuthenticatedUser_shouldCreateEvent(
        test_user, authenticated_client):
    # Arrange
    event_data_copy = event_data.copy()
    event_data_copy['organizer'] = test_user.id

    # Act
    response = authenticated_client.post('/api/events/', event_data_copy, format='json')

    # Assert
    assert response.status_code == status.HTTP_201_CREATED
    assert Event.objects.count() == 1
    assert Event.objects.get().title == event_data['title']


@pytest.mark.django_db
@pytest.mark.parametrize('field, invalid_value',
                         [('title', ''),
                          ('organizer', -1),
                          ('date', 'invalid_date'),
                          ('date', ''),
                          ('time', 'invalid_time'),
                          ('time', ''),
                          ('event_type', 'invalid_event_type'),
                          ('event_type', ''),
                          ('location', ''),
                          ('ticket_price', 'invalid_ticket_price'),
                          ('ticket_price', '')])
def testEventCreation_withInvalidDetails_byAuthenticatedUser_shouldNotCreateEvent(
        test_user, authenticated_client, field, invalid_value):
    # Arrange
    event_data_copy = event_data.copy()
    event_data_copy['organizer'] = test_user.id
    event_data_copy[field] = invalid_value

    # Act
    response = authenticated_client.post('/api/events/', event_data_copy, format='json')

    # Assert
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert Event.objects.count() == 0


@pytest.mark.django_db
def testEventCreation_withValidDetails_byUnauthenticatedUser_shouldNotCreateEvent(test_user):
    # Arrange
    unauthenticated_client = APIClient()
    event_data_copy = event_data.copy()
    event_data_copy['organizer'] = test_user.id

    # Act
    response = unauthenticated_client.post('/api/events/', event_data_copy, format='json')

    # Assert
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert Event.objects.count() == 0


@pytest.mark.django_db
def testEventRetrieval_withValidEventId_byAuthenticatedUser_shouldRetrieveEvent(test_event, test_user):
    # Arrange
    unauthenticated_client = APIClient()

    # Act
    response = unauthenticated_client.get(f'/api/events/{test_event.id}/')

    # Assert
    assert response.status_code == status.HTTP_200_OK
    response.data.pop('created_at')
    response.data.pop('updated_at')
    response.data.pop('cover_image')
    assert response.data == {'title': event_data['title'],
                             'organizer': test_user.id,
                             'description': event_data['description'],
                             'date': event_data['date'],
                             'email': '',
                             'event_type': 'virtual',
                             'location': 'test location',
                             'time': '00:00:00',
                             'phone': '',
                             'ticket_price': '0.00'
                             }


@pytest.mark.django_db
def testEventRetrieval_withInvalidEventId_shouldThrowNotFound(test_event):
    # Arrange
    unauthenticated_client = APIClient()

    # Act
    response = unauthenticated_client.get(f'/api/events/{test_event.id + 1}/')

    # Assert
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def testListEventsView_shouldListEvents(test_event):
    # Arrange
    unauthenticated_client = APIClient()

    # Act
    response = unauthenticated_client.get('/api/events/')

    # Assert
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    response.data[0].pop('created_at')
    response.data[0].pop('updated_at')
    response.data[0].pop('cover_image')
    assert response.data[0] == {'title': event_data['title'],
                                'organizer': test_event.organizer.id,
                                'description': event_data['description'],
                                'date': event_data['date'],
                                'email': '',
                                'event_type': 'virtual',
                                'location': 'test location',
                                'time': '00:00:00',
                                'phone': '',
                                'ticket_price': '0.00'
                                }


@pytest.mark.django_db
def testEventUpdate_withValidEventId_byOwner_shouldUpdateEvent(
        test_user, authenticated_client, test_event):
    # Arrange
    event_data_copy = event_data.copy()
    event_data_copy['title'] = 'updated title'
    event_data_copy['organizer'] = test_user.id
    event_data_copy['date'] = '2021-01-02'

    # Act
    response = authenticated_client.put(f'/api/events/{test_event.id}/',
                                        event_data_copy, format='json')

    # Assert
    assert response.status_code == status.HTTP_200_OK
    assert response.data['title'] == 'updated title'
    assert response.data['date'] == '2021-01-02'
    assert Event.objects.get().title == 'updated title'
    assert Event.objects.get().date.strftime('%Y-%m-%d') == '2021-01-02'


@pytest.mark.django_db
def testEventUpdate_withValidEventId_byNonOwner_shouldThrowForbidden(
        authenticated_client):
    # Arrange 
    account_data_copy = account_data.copy()
    account_data_copy['email'] = 'changed@email.com'
    test_user_2 = Account.objects.create(**account_data_copy)
    event_data_copy = event_data.copy()
    event_data_copy['organizer'] = test_user_2
    event = Event.objects.create(**event_data_copy)

    event_data_copy['title'] = 'updated title'
    event_data_copy['organizer'] = test_user_2.id

    # Act
    response = authenticated_client.put(f'/api/events/{event.id}/', event_data_copy, format='json')

    # Assert
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert Event.objects.get().title == event_data['title']


@pytest.mark.django_db
def testEventUpdate_withInvalidEventId_shouldThrowNotFound(
        test_user, authenticated_client, test_event):
    # Arrange
    event_data_copy = event_data.copy()
    event_data_copy['title'] = 'updated title'
    event_data_copy['organizer'] = test_user.id

    # Act
    response = authenticated_client.put(f'/api/events/{test_event.id + 1}/',
                                        event_data_copy, format='json')

    # Assert
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def testEventDelete_withValidEventId_byOwner_shouldDeleteEvent(authenticated_client, test_event):
    # Arrange
    # Act
    response = authenticated_client.delete(f'/api/events/{test_event.id}/')

    # Assert
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Event.objects.count() == 0


@pytest.mark.django_db
def testEventDelete_withValidEventId_byNonOwner_shouldThrowForbidden(
        authenticated_client):
    # Arrange   
    account_data_copy = account_data.copy()
    account_data_copy['email'] = 'new@email.com'
    test_user_2 = Account.objects.create(**account_data_copy)

    event_data_copy = event_data.copy()
    event_data_copy['organizer'] = test_user_2
    event = Event.objects.create(**event_data_copy)

    # Act
    response = authenticated_client.delete(f'/api/events/{event.id}/')

    # Assert
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert Event.objects.count() == 1


@pytest.mark.django_db
def testEventDelete_withInvalidEventId_shouldThrowNotFound(authenticated_client, test_event):
    # Arrange
    # Act
    response = authenticated_client.delete(f'/api/events/{test_event.id + 1}/')

    # Assert
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert Event.objects.count() == 1
