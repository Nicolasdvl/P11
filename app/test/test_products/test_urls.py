from django.test import Client, TestCase, override_settings
from products.models import Product
from authentification.models import User


@override_settings(
    STATICFILES_STORAGE="django.contrib.staticfiles.storage.StaticFilesStorage"
)
class TestProductsUrls(TestCase):
    """Test urls from products app."""

    fixtures = [
        "test_users.json",
        "test_products.json",
        "test_categories.json",
    ]

    @classmethod
    def setUpTestData(cls):
        """Initiate objects for tests."""
        cls.product = Product.objects.get(id=1)
        cls.user = User.objects.get(id=1)
        cls.saves = cls.user.get_saves()
        cls.subs = cls.product.get_subs_list()
        cls.similar = Product.objects.filter(name__icontains="coca")

    def setUp(self):
        """Initiate django client test."""
        self.client = Client()

    def test_substitutes(self):
        """
        Test 'product/<int:id>'.

        1/ GET status should be 200.
        2/ Context should have product object.
        3/ Context should have substitutes list.
        """
        response = self.client.get("/product/1/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["product"], self.product)
        self.assertEqual(response.context["substitutes"], self.subs)

    def test_similar(self):
        """
        Test 'product/'.

        1/ POST status should be 200.
        2/ Context should have similar_products with objects.
        3/ POST status should be 200.
        4/ Context shouldn't have object in similar_products.
        """
        response_with_similar_products = self.client.post(
            "/product/", data={"search_input": "coca"}
        )
        response_without_similar_products = self.client.post(
            "/product/", data={"search_input": "inexistant"}
        )
        self.assertEqual(response_with_similar_products.status_code, 200)
        self.assertQuerysetEqual(
            response_with_similar_products.context["similar_products"],
            self.similar,
            ordered=False,
        )
        self.assertEqual(response_without_similar_products.status_code, 200)
        self.assertQuerysetEqual(
            response_without_similar_products.context["similar_products"], []
        )

    def test_claim(self):
        """
        Test '/claim'.

        1/ GET status with unauth user should redirect on login page.
        2/ GET status with auth user should be 200.
        """
        response_unauth = self.client.get("/claim/")
        self.client.login(email="john@email.com", password="mdp")
        response_auth = self.client.get("/claim/")
        self.assertRedirects(response_unauth, "/login")
        self.assertEqual(response_auth.status_code, 200)

    def test_details(self):
        """
        Test 'product/<int:id>/details'.

        1/ GET status should be 200.
        2/ Context should have product object.
        """
        response = self.client.get("/product/1/details/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["product"], self.product)

    def test_my_substitutes(self):
        """
        Test 'account/my_substitutes'.

        1/ GET status with unauth user should redirect on login page.
        2/ GET status with auth user should be 200.
        3/ Context should have a list of products saved.
        """
        response_unauth = self.client.get("/account/my_substitutes/")
        self.client.login(email="john@email.com", password="mdp")
        response_auth = self.client.get("/account/my_substitutes/")

        self.assertRedirects(response_unauth, "/login")
        self.assertEqual(response_auth.status_code, 200)
        self.assertEqual(response_auth.context["products"], self.saves)
