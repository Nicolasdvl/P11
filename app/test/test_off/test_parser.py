from unittest.mock import MagicMock, patch
from django.test import TestCase
from off.off_parser import Parser
import requests
import json


class SetUpMocks:
    """Construct mocks for tests."""

    def __init__(self):
        """Initialize mocks."""
        self.fake_response = MagicMock()
        self.fake_response.json.return_value = self.return_fake_json()
        self.fake_get = MagicMock(return_value=self.fake_response)

    def return_fake_json(self):
        """Load a fake response from 'mock_requests.json'."""
        with open("app/test/test_off/mock_requests.json", "r") as file:
            content = json.load(file)
        return content


class TestRequests(TestCase):
    mocks = SetUpMocks()

    @patch("requests.get", mocks.fake_get)
    def setUp(self):
        self.expected_formated_data = [
            {
                "3274080005003": {
                    "name": "Cristaline Eau de source",
                    "brand": "Cristaline",
                    "nutriscore": "A",
                    "categories": [
                        "en:beverages",
                        "en:waters",
                        "en:spring-waters",
                        "en:mineral-waters",
                        "en:natural-mineral-waters",
                    ],
                    "image": "https://images.openfoodfacts.org/images/products/327/408/000/5003/front_fr.786.400.jpg",
                }
            },
            {
                "7622210449283": {
                    "name": "Prince Chocolat",
                    "brand": "LU,MONDELEZ",
                    "nutriscore": "D",
                    "categories": [
                        "en:snacks",
                        "en:sweet-snacks",
                        "en:biscuits-and-cakes",
                        "en:biscuits",
                        "en:chocolate-biscuits",
                    ],
                    "image": "https://images.openfoodfacts.org/images/products/762/221/044/9283/front_fr.437.400.jpg",
                }
            },
        ]
        self.parser = Parser()
        self.data = requests.get("off_url&params").json()
        self.products = self.data["products"]

    @patch("requests.get", mocks.fake_get)
    def test_mock_request(self):
        """
        Test if mocks works.

        Requests mock should return a response with json which contain
        3 products.
        """
        response = requests.get("off_url&params")
        data = response.json()
        self.assertIn("products", data)
        self.assertEqual(len(data["products"]), 3)

    def test_is_it_valid(self):
        """
        Test if Parser.is_it_valid() work.

        The function should valid first and second product
        and invalid the third product which doesn't have image.
        """

        # Arrange
        first_product = self.products[0]
        second_product = self.products[1]
        third_product = self.products[2]
        # Act
        first_result = self.parser.is_it_valid(first_product)
        second_result = self.parser.is_it_valid(second_product)
        third_result = self.parser.is_it_valid(third_product)
        # Assert
        self.assertTrue(first_result)
        self.assertTrue(second_result)
        self.assertFalse(third_result)

    def test_formate(self):
        """
        Test if Parser.formate() work.

        The function should return formated data contain in expected_formated_data.
        """
        # Arrange
        for product in self.products:
            if self.parser.is_it_valid(product):
                # Act
                formated_data = self.parser.formate(product)
                # Assert
                self.assertIn(formated_data, self.expected_formated_data)
