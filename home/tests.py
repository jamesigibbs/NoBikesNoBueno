from django.urls import reverse
from django.test import TestCase, Client
# Create your tests here.


class TemplateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
    

    def test_index_template_returned(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Our Merch")

