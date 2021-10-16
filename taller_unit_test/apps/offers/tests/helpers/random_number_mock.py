from unittest.mock import Mock

def request_get_returns_20():
    requestsMock=Mock()

    json_response_mock = Mock()
    json_response_mock.json.return_value = [{"random": 20}]

    requestsMock.get.return_value = json_response_mock

    return requestsMock
