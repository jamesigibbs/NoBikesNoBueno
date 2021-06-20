from django.urls import reverse
from django.test import TestCase, Client

# Create your tests here.

class TemplateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
    

    def test_riders_template_returned(self):
        response = self.client.get(reverse('riders'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No Bikes No Bueno")
