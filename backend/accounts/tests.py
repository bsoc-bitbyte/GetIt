import pytest
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework import status
from rest_framework.test import APIClient

from .models import Account
from .token import account_activation_token

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

    # check that the account is inactive initially 
    assert not Account.objects.get().is_active


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
def testActivate_invalidTokenOrUid_returnsBadRequest():
    # Arrange
    client = APIClient()
    account = Account.objects.create(**account_data)
    token = account_activation_token.make_token(account)
    uid = urlsafe_base64_encode(force_bytes(account.email))

    # Act
    response = client.post(f'/api/accounts/activate/{uid}/malformed{token}')
    print(response.content,response)
    # Assert
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert not Account.objects.get().is_active


@pytest.mark.django_db
def testActivate_validTokenAndUid_accountActivated():
    # Arrange
    client = APIClient()
    account = Account.objects.create(**account_data)
    token = account_activation_token.make_token(account)
    uid = urlsafe_base64_encode(force_bytes(account.email))

    # Act
    response = client.post(f'/api/accounts/activate/{uid}/{token}')

    # Assert
    assert response.status_code == status.HTTP_200_OK
    assert Account.objects.get().is_active

@pytest.mark.django_db
def testRetrieveLoggedInAccountView_userLoggedIn_returnsAccountDetails(api_client):
    # Act
    response = api_client.get('/api/accounts/me/', format='json')

    # Assert
    assert response.status_code == status.HTTP_200_OK
    assert response.data['email'] == account_data['email']


@pytest.mark.django_db
def testRetrieveLoggedInAccountView_userNotLoggedIn_returnsUnauthorized():
    # Arrange
    client = APIClient()

    # Act
    response = client.get('/api/accounts/me/', format='json')

    # Assert
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


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
def testUpdateLogInAccountView_userNotLoggedIn_returnsUnauthorized():
    # Arrange
    client = APIClient()

    # Act
    response = client.put('/api/accounts/me/', {}, format='json')

    # Assert
    assert response.status_code == status.HTTP_401_UNAUTHORIZED