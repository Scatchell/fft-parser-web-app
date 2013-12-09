import json
import urllib2
import redis

class Parser(object):
    def __init__(self):
        self.db = redis.StrictRedis(host='localhost', port=6379, db=0)

    def refresh_data(self):
        self.db.flushdb()
        orders_list = json.loads(urllib2.urlopen('http://tw-food-for-thought.herokuapp.com/information/orders.js').read())
        for order in orders_list:
            self.db.hmset(order['id'], order)

    def load_data(self):
        orders_list = []
        for key in self.db.keys():
            orders_list.append(self.db.hgetall(key))
        print orders_list
        #fft_data =
        #self.fft_orders = json.load(fft_data)

    def load_from_json(self, json_data):
        self.fft_orders = json.loads(json_data)

    def print_list(self):
        print self.fft_orders

    def user_ids_from_orders(self, orders):
        user_ids = []
        if orders:
            for element in orders:
                user_ids.append(element['user_id'])
        return user_ids

#class Order(object):
#    def name(self, hello, godbye)
#        hello

#load each order into an order object

#have some parser object that can find, given a list of orders, the user id of the order with the most items
