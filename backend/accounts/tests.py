import pytest
from rest_framework.test import APIClient
from rest_framework import status
from .models import Account

account_data = {
    "email": "test@email.com",
    "password": "testpassword",
    "first_name": "test",
    "last_name": "account",
    "phone_number": "1234567890",
    "address": "test address",
    }


@pytest.fixture
def api_client():
    account = Account.objects.create(**account_data)
    client = APIClient()
    client.force_authenticate(user=account)
    return client


@pytest.mark.django_db
def testCreateAccountView_validAccountDetails_accountCreationSuccesful():
    # Arrange
    client = APIClient()

    # Act
    response = client.post('/api/accounts/', account_data, format='json')

    print(response.data)

    # Assert
    assert response.status_code == status.HTTP_201_CREATED
    assert Account.objects.count() == 1
    assert response.data['email'] == account_data['email']

    # check that password is not returned and the stored password is hashed
    assert 'password' not in response.data
    assert Account.objects.get().password != account_data['password']


@pytest.mark.django_db
@pytest.mark.parametrize('field', ['email', 'password', 'first_name', 'last_name'])
def testCreateAccountView_missingRequiredDetails_returnsBadRequest(field):
    # Arrange
    client = APIClient()
    data = account_data.copy()
    data.pop(field)

    # Act
    response = client.post('/api/accounts/', data, format='json')

    # Assert
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
@pytest.mark.parametrize('new_email', ['test@email.com', 'testemail'])
def testCreateAccountView_invalidOrDuplicateEmail_returnsBadRequest(new_email):
    # Arrange
    client = APIClient()
    client.post('/api/accounts/', account_data, format='json')
    data = account_data.copy()
    data['email'] = new_email

    # Act
    response = client.post('/api/accounts/', data, format='json')

    # Assert
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def testRetrieveLoggedInAccountView_userLoggedIn_returnsAccountDetails(api_client):
    # Act
    response = api_client.get('/api/accounts/me/', format='json')

    # Assert
    assert response.status_code == status.HTTP_200_OK
    assert response.data['email'] == account_data['email']


@pytest.mark.django_db
def testRetrieveLoggedInAccountView_userNotLoggedIn_returnsForbidden():
    # Arrange
    client = APIClient()

    # Act
    response = client.get('/api/accounts/me/', format='json')

    # Assert
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
@pytest.mark.parametrize('field', ['email', 'first_name', 'last_name', 'address'])
def testUpdateLogInAccountView_userLoggedIn_updateSuccesful(api_client, field):
    # Arrange
    data = {
        field: f'new{account_data[field]}'
    }

    # Act
    response = api_client.put('/api/accounts/me/', data, format='json')

    # Assert
    assert response.status_code == status.HTTP_200_OK
    assert response.data[field] == data[field]


@pytest.mark.django_db
def testUpdateLogInAccountView_userNotLoggedIn_returnsForbidden():
    # Arrange
    client = APIClient()

    # Act
    response = client.put('/api/accounts/me/', {}, format='json')

    # Assert
    assert response.status_code == status.HTTP_403_FORBIDDEN
