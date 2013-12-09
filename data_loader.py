import redis
import json
import urllib2



class DataLoader:
    def __init__(self):
        self.db = redis.StrictRedis(host='localhost', port=6379, db=0)

    def refresh_data(self):
        self.db.flushdb()
        orders_list = json.loads(urllib2.urlopen('http://tw-food-for-thought.herokuapp.com/information/orders.js').read())
        for order in orders_list:
            self.db.hmset("order_" + str(order['id']), order)

        users_list = json.loads(urllib2.urlopen('http://tw-food-for-thought.herokuapp.com/information/users.js').read())
        for user in users_list:
            self.db.hmset("user_" + str(user['id']), user)

    def load_order_list(self):
        orders_list = []
        for key in self.db.keys("order_*"):
            orders_list.append(self.db.hgetall(key))
        return orders_list

    def load_user_list(self):
        user_list = []
        for key in self.db.keys("user_*"):
            user_list.append(self.db.hgetall(key))
        return user_list