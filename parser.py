from order import Order
import json

class Parser:
	def __init__(self, order_dict_list):
		self.order_list = [] 
		for order_dict in order_dict_list:
			order = Order(order_dict)
			self.order_list.append(order)

		print len(self.order_list)

	def biggest_order(self):
		max_value = 0
		for order in self.order_list:
			if max_value < order.number_of_items():
				max_value = order.number_of_items()

		return max_value

	def order_list_with_num_of_items(self, num_of_items):
		biggest_order_list = []
		for order in self.order_list:
			if order.number_of_items() == num_of_items:
				biggest_order_list.append(order)

		return biggest_order_list


	def most_expensive_order(self):
	    total_order_price = 0
	    for order in self.order_list:
	    	print order
	        if total_order_price < order.total_price():
	        	total_order_price = order.total_price()
	        	most_expensive_order = order

	    return most_expensive_order

	def users_who_ordered_most_of(self, item_id): # n.b: yet to be refactored
		order_item_list = self.orders_with_item(item_id)		

		user_and_num_ordered = self.num_of_items_ordered_per_user(order_item_list)
		max_no_ordered =  max(user_and_num_ordered.values())

		users_with_max_orders = self.list_of_users_with_max_orders(user_and_num_ordered, max_no_ordered)

		return users_with_max_orders

	def orders_with_item(self,item_id):
		order_item_list = []
		for order in self.order_list:
			if len(filter (lambda x : x.id == item_id, order.items)) > 0:
				order_item_list.append(order)

		return order_item_list

	def num_of_items_ordered_per_user(self,order_item_list):
		user_and_num_ordered = {}
		for order in order_item_list:
			if user_and_num_ordered.has_key(order.user_id):
				user_and_num_ordered[order.user_id] = user_and_num_ordered[order.user_id] + 1
			else:
				user_and_num_ordered.update({order.user_id : 1})

		return user_and_num_ordered

	def list_of_users_with_max_orders(self,user_and_num_ordered,max_no_ordered):
		users_with_max_orders = {}

		for key, value in user_and_num_ordered.iteritems():
			if value == max_no_ordered:
				users_with_max_orders.update({key: value})
		return users_with_max_orders

	def user_who_has_paid_highest(self):
		users_and_overall_total_price = self.users_and_overall_total_price()
		highest_price = max(users_and_overall_total_price.values())
		return self.users_with_overall_highest_total_price(users_and_overall_total_price, highest_price)



	def users_and_overall_total_price(self):
		users_and_overall_total_price = {}
		for order in self.order_list:
			if not order.user_id <= 1:
				if users_and_overall_total_price.has_key(order.user_id):
					users_and_overall_total_price[order.user_id] += order.total_price()
				else:
					users_and_overall_total_price.update({order.user_id : order.total_price()})

		return users_and_overall_total_price

	def users_with_overall_highest_total_price(self, users_and_overall_total_price, highest_price):
		users_with_overall_highest_total_price = {}
		for key, value in users_and_overall_total_price.iteritems():
			if value == highest_price:
				users_with_overall_highest_total_price.update({key : value})

		return users_with_overall_highest_total_price



