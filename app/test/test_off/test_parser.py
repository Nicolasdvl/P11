from itertools import product
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

    mocks = SetUpMocks()

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

    @patch("requests.get", mocks.fake_get)
    def test_is_it_valid(self):
        data = requests.get("off_url&params").json()
        parser = Parser()
        # First and second products are valid
        self.assertTrue(parser.is_it_valid(data["products"][0]))
        self.assertTrue(parser.is_it_valid(data["products"][1]))
        # Third product is invalid because it doesn't have image.
        self.assertFalse(parser.is_it_valid(data["products"][2]))

    @patch("requests.get", mocks.fake_get)
    def test_formate(self):
        data = requests.get("off_url&params").json()
        parser = Parser()
        products = data["products"]
        for product in products:
            formated_data = parser.formate(product)
            self.assertIn(formated_data, self.expected_formated_data)
