import unittest
import json
from src.item import Item
from src.order import Order
from src.parser import Parser

class TestParser(unittest.TestCase):

    def setUp(self):
        orders_json = """
        [
	        {"id":1,"created_at":"2013-10-06T09:55:46.385Z","updated_at":"2013-10-10T15:08:15.198Z","user_id":7,"items":[{"id":4,"name":"Another item","price":1000,"created_at":"2013-09-30T19:08:53.228Z","updated_at":"2013-10-20T10:02:56.701Z","available":true,"item_type":"food"}]},
	        {"id":2,"created_at":"2013-10-06T09:55:46.396Z","updated_at":"2013-10-10T15:08:15.201Z","user_id":7,"items":[{"id":2,"name":"Pizza","price":3000,"created_at":"2013-09-29T11:20:31.997Z","updated_at":"2013-10-10T11:57:59.212Z","available":false,"item_type":"food"}]},
	        {"id":3,"created_at":"2013-10-06T09:55:46.401Z","updated_at":"2013-10-10T15:08:15.203Z","user_id":7,"items":[{"id":2,"name":"Pizza","price":3000,"created_at":"2013-09-29T11:20:31.997Z","updated_at":"2013-10-10T11:57:59.212Z","available":false,"item_type":"food"}]},
	        {"id":4,"created_at":"2013-10-06T09:55:46.405Z","updated_at":"2013-10-10T15:08:15.205Z","user_id":7,"items":[{"id":2,"name":"Pizza","price":3000,"created_at":"2013-09-29T11:20:31.997Z","updated_at":"2013-10-10T11:57:59.212Z","available":false,"item_type":"food"},{"id":8,"name":"Chicken","price":5000,"created_at":"2013-10-04T07:46:12.103Z","updated_at":"2013-10-20T10:02:56.703Z","available":true,"item_type":"meat"},{"id":10,"name":"Beer","price":3000,"created_at":"2013-10-04T07:46:34.873Z","updated_at":"2013-10-20T10:02:56.702Z","available":true,"item_type":"drink"}]},
	        {"id":5,"created_at":"2013-10-06T09:55:46.411Z","updated_at":"2013-10-10T15:08:15.206Z","user_id":7,"items":[{"id":9,"name":"Beef","price":5000,"created_at":"2013-10-04T07:46:18.611Z","updated_at":"2013-10-10T11:57:59.217Z","available":false,"item_type":"meat"}]},
	        {"id":6,"created_at":"2013-10-06T10:06:27.506Z","updated_at":"2013-10-10T15:08:15.207Z","user_id":7,"items":[{"id":2,"name":"Pizza","price":3000,"created_at":"2013-09-29T11:20:31.997Z","updated_at":"2013-10-10T11:57:59.212Z","available":false,"item_type":"food"},{"id":8,"name":"Chicken","price":5000,"created_at":"2013-10-04T07:46:12.103Z","updated_at":"2013-10-20T10:02:56.703Z","available":true,"item_type":"meat"},{"id":10,"name":"Beer","price":3000,"created_at":"2013-10-04T07:46:34.873Z","updated_at":"2013-10-20T10:02:56.702Z","available":true,"item_type":"drink"}]},
	        {"id":10,"created_at":"2013-10-10T11:57:59.200Z","updated_at":"2013-10-10T15:08:15.208Z","user_id":7,"items":[{"id":2,"name":"Pizza","price":3000,"created_at":"2013-09-29T11:20:31.997Z","updated_at":"2013-10-10T11:57:59.212Z","available":false,"item_type":"food"},{"id":8,"name":"Chicken","price":5000,"created_at":"2013-10-04T07:46:12.103Z","updated_at":"2013-10-20T10:02:56.703Z","available":true,"item_type":"meat"},{"id":9,"name":"Beef","price":5000,"created_at":"2013-10-04T07:46:18.611Z","updated_at":"2013-10-10T11:57:59.217Z","available":false,"item_type":"meat"}]},
	        {"id":11,"created_at":"2013-10-10T15:17:53.655Z","updated_at":"2013-10-10T15:17:53.655Z","user_id":7,"items":[{"id":11,"name":"This is a long item","price":1000,"created_at":"2013-10-04T07:52:15.889Z","updated_at":"2013-10-20T10:02:56.700Z","available":true,"item_type":"drink"},{"id":13,"name":"Veggie","price":2000,"created_at":"2013-10-04T16:12:22.997Z","updated_at":"2013-10-10T15:17:53.717Z","available":false,"item_type":"vegetable"},{"id":12,"name":"Test meat item","price":1000,"created_at":"2013-10-04T16:11:52.087Z","updated_at":"2013-10-20T10:02:56.706Z","available":true,"item_type":"meat"}]},
	        {"id":12,"created_at":"2013-10-10T15:17:53.684Z","updated_at":"2013-10-10T15:17:53.684Z","user_id":7,"items":[{"id":2,"name":"Pizza","price":3000,"created_at":"2013-09-29T11:20:31.997Z","updated_at":"2013-10-10T11:57:59.212Z","available":false,"item_type":"food"},{"id":9,"name":"Beef","price":5000,"created_at":"2013-10-04T07:46:18.611Z","updated_at":"2013-10-10T11:57:59.217Z","available":false,"item_type":"meat"},{"id":8,"name":"Chicken","price":5000,"created_at":"2013-10-04T07:46:12.103Z","updated_at":"2013-10-20T10:02:56.703Z","available":true,"item_type":"meat"}]},
	        {"id":13,"created_at":"2013-10-10T15:17:53.692Z","updated_at":"2013-10-10T15:17:53.692Z","user_id":7,"items":[{"id":10,"name":"Beer","price":3000,"created_at":"2013-10-04T07:46:34.873Z","updated_at":"2013-10-20T10:02:56.702Z","available":true,"item_type":"drink"},{"id":9,"name":"Beef","price":5000,"created_at":"2013-10-04T07:46:18.611Z","updated_at":"2013-10-10T11:57:59.217Z","available":false,"item_type":"meat"},{"id":15,"name":"Meat Item","price":5000,"created_at":"2013-10-07T15:48:52.017Z","updated_at":"2013-10-20T10:02:56.705Z","available":true,"item_type":"meat"}]},
	        {"id":14,"created_at":"2013-10-10T15:17:53.702Z","updated_at":"2013-10-10T15:17:53.702Z","user_id":4,"items":[{"id":13,"name":"Veggie","price":2000,"created_at":"2013-10-04T16:12:22.997Z","updated_at":"2013-10-10T15:17:53.717Z","available":false,"item_type":"vegetable"},{"id":8,"name":"Chicken","price":5000,"created_at":"2013-10-04T07:46:12.103Z","updated_at":"2013-10-20T10:02:56.703Z","available":true,"item_type":"meat"},{"id":15,"name":"Meat Item","price":5000,"created_at":"2013-10-07T15:48:52.017Z","updated_at":"2013-10-20T10:02:56.705Z","available":true,"item_type":"meat"}]}
        ]"""
        self.parser = Parser(orders_json)

    def test_should_find_the_order_with_most_items(self):
    	self.assertEqual(self.parser.biggest_order(), 3)

    def test_should_return_biggest_orders(self):
    	self.assertEqual(len(self.parser.order_list_with_num_of_items(3)), 7)

    def test_should_return_users_who_ordered_most_of_item(self):
    	user_and_times_ordered = self.parser.users_who_ordered_most_of(8)
    	self.assertTrue(user_and_times_ordered.has_key(7))
    	self.assertEqual(user_and_times_ordered[7], 4)

    def test_should_return_the_user_who_has_paid_the_highest_amount(self):
    	user_who_has_paid_highest = self.parser.user_who_has_paid_highest();
    	print user_who_has_paid_highest
    	self.assertTrue(user_who_has_paid_highest.has_key(7))





if __name__ == '__main__':
	unittest.main()
