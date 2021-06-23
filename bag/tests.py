from django.urls import reverse
from django.test import TestCase, Client


class TemplateViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_bag_template_returned(self):
        response = self.client.get(reverse('bag_view'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Your Cart")
