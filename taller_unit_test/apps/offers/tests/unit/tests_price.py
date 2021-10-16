from django.test import TransactionTestCase
from unittest.mock import patch, Mock

from taller_unit_test.apps.offers.tests.helpers.random_number_mock import request_get_returns_20
from taller_unit_test.apps.offers import price as priceService

NUMBER_OFFERS_TO_CREATE = 3


class OfferPriceTestCase(TransactionTestCase):
    def setUp(self):
        requestsMock=Mock()

        json_response_mock = Mock()
        json_response_mock.json.return_value = [{"random": 20}]

        requestsMock.get.return_value = json_response_mock

    @patch("taller_unit_test.apps.offers.price.requests", new=request_get_returns_20())
    def test_get_random_number_send_a_request_to_api_and_returns_random_key(self):
        random_number = priceService.get_random_number()

        self.assertEqual(random_number, 20)

    @patch("taller_unit_test.apps.offers.price.requests", new=request_get_returns_20())
    def test_calculate_price_return_price_multiplied_by_random_number(self):
        initial_price = 100

        calculated_price = priceService.calculate_price(initial_price)

        self.assertEqual(calculated_price, 2000)
