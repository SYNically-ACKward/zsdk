import pytest
from unittest.mock import Mock, patch, _ANY
from zsdk.zia import zia


def test_authenticate():
    # Simulate the API's response
    mock_response = Mock()
    mock_response.headers = {'JSESSIONID': 'value'}

    # Patching the _request function
    with patch('zsdk.zia._request') as mock_request:
        mock_request.return_value = mock_response

        # Create an instance of the class
        instance = zia(username='user@example.com', password='pass1234', api_key='A1B2c3D4eF12', cloud_name='zscaler.net')

        # Call the method you're testing
        instance._authenticate()

        # Assertions to check the behavior
        # assert instance._session.cookies['JSESSIONID'] == 'value'
        mock_request.assert_called_once_with(
            session=instance._session,
            method="post",
            url="zsapi.zscaler.net/api/v1/authenticatedSession",
            json={'apiKey': 'A1B2c3D4eF12', 'username': 'user@example.com', 'password': 'pass1234', 'timestamp': _ANY}
        )
