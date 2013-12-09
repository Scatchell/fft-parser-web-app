import unittest
import json
from src.item import Item
from src.order import Order

class TestParser(unittest.TestCase):

    def setUp(self):
		item_json = '{"id":4,"name":"Another item","price":1000,"created_at":"2013-09-30T19:08:53.228Z","updated_at":"2013-10-20T10:02:56.701Z","available":true,"item_type":"food"}'
		self.item_hash = json.loads(item_json)


    def test_item_should_load_from_hash(self):
        item = Item(self.item_hash)
        self.assertEqual(item.id, 4)
        self.assertEqual(item.name, "Another item")
        self.assertEqual(item.price, 1000)
        self.assertEqual(item.available,True)

if __name__ == '__main__':
    unittest.main()