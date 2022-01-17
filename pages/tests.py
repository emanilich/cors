from django.contrib.auth import get_user_model
from django.test import SimpleTestCase, TestCase
from django.urls import reverse

# Create your tests here.
class HomePageTests(SimpleTestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().object.create_user(
            username="testuser",
            email="test@email.com",
            password="secret"
        )
    
    def test_homepage_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_homepage_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "Home")
