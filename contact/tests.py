from django.urls import reverse
from django.test import TestCase, Client


class TemplateViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_contact_template_returned(self):
        response = self.client.get(reverse('contact'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Contact Us")
