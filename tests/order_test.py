import unittest
import json
from src.item import Item
from src.order import Order

class TestParser(unittest.TestCase):

    def setUp(self):
        self.order_json = '{"id":1,"created_at":"2013-10-06T09:55:46.385Z","updated_at":"2013-10-10T15:08:15.198Z","user_id":7,"items":[{"id":4,"name":"Another item","price":1000,"created_at":"2013-09-30T19:08:53.228Z","updated_at":"2013-10-20T10:02:56.701Z","available":true,"item_type":"food"}]}'

    def test_order_should_load_from_hah(self):
        order = Order(json.loads(self.order_json))
        self.assertEqual(order.id,1)
        self.assertEqual(order.user_id,7)
        self.assertEqual(order.items[0].id, 4)

    def test_no_of_order_items(self):
        order = Order(json.loads(self.order_json))
        self.assertEqual(len(order.items),1)


if __name__ == '__main__':
    unittest.main()
