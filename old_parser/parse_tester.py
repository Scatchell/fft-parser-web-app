import unittest
import json
from item import Item
from parse import Parser

class TestParser(unittest.TestCase):

    def setUp(self):
        order_json = '[{"id":1,"created_at":"2013-10-06T09:55:46.385Z","updated_at":"2013-10-10T15:08:15.198Z","user_id":7,"items":[{"id":4,"name":"Another item","price":1000,"created_at":"2013-09-30T19:08:53.228Z","updated_at":"2013-10-20T10:02:56.701Z","available":true,"item_type":"food"}]},{"id":2,"created_at":"2013-10-06T09:55:46.396Z","updated_at":"2013-10-10T15:08:15.201Z","user_id":8,"items":[{"id":2,"name":"Pizza","price":3000,"created_at":"2013-09-29T11:20:31.997Z","updated_at":"2013-10-10T11:57:59.212Z","available":false,"item_type":"food"}]},{"id":3,"created_at":"2013-10-06T09:55:46.401Z","updated_at":"2013-10-10T15:08:15.203Z","user_id":9,"items":[{"id":2,"name":"Pizza","price":3000,"created_at":"2013-09-29T11:20:31.997Z","updated_at":"2013-10-10T11:57:59.212Z","available":false,"item_type":"food"}]},{"id":4,"created_at":"2013-10-06T09:55:46.405Z","updated_at":"2013-10-10T15:08:15.205Z","user_id":1,"items":[{"id":2,"name":"Pizza","price":3000,"created_at":"2013-09-29T11:20:31.997Z","updated_at":"2013-10-10T11:57:59.212Z","available":false,"item_type":"food"},{"id":8,"name":"Chicken","price":5000,"created_at":"2013-10-04T07:46:12.103Z","updated_at":"2013-10-20T10:02:56.703Z","available":true,"item_type":"meat"},{"id":10,"name":"Beer","price":3000,"created_at":"2013-10-04T07:46:34.873Z","updated_at":"2013-10-20T10:02:56.702Z","available":true,"item_type":"drink"}]}]'
        self.order_hash = json.loads(order_json)

    def test_item_should_load_from_hash(self):
        item = Item(self.order_hash[0]['items'][0])
        self.assertEqual(item.identifier, 4)
        self.assertEqual(item.name, "Another item")
        self.assertEqual(item.price, 1000)

#    def test_order_should_load_from_hah(self):
#        order = Order(order_hash)
#        self.assertEqual(order.identifier,1)
#        self.assertEqual(order.user_id,7)
#        self.assertEqual(order.items[0].identifier, 4)

    def test_parse_user_ids(self):
        parser = Parser()
        parser.fft_orders = self.order_hash
        self.assertEqual([7,8,9,1], parser.user_ids_from_orders(parser.fft_orders))

if __name__ == '__main__':
    unittest.main()
