from django.test import Client, TestCase

from .models import Item


# Create your tests here.
class ItemTestCase(TestCase):
    def setUp(self):
        Item.objects.create(name="test", amount=1, description="test")

    def test_inventory_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_inventory_using_inventory_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'inventory_main.html')

    def test_item(self):
        item = Item.objects.get(name="test")
        self.assertEqual(item.name, 'test')
        self.assertEqual(item.amount, 1)
        self.assertEqual(item.description, 'test')