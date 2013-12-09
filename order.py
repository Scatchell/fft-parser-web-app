import ast
import json
from item import Item

class Order:
    def __init__(self, order_dict):
        self.id = order_dict['id']
        self.user_id =order_dict['user_id']
        self.items = []
        item_list = ast.literal_eval(order_dict['items'])
        for item_dict in item_list:
            self.items.append(Item(item_dict))

    def number_of_items(self):
    	return len(self.items)

    def total_price(self):
    	total_price = 0
    	for item in self.items:
    		total_price += item.price 
    	return total_price
