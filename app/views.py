from app import app
from parser import Parser
from data_loader import DataLoader
from user_list import UserList

@app.route('/')
@app.route('/index')
def index():
    return "This is the food for thought parser. Find out how much money you have wasted on mediocre food."

@app.route('/most_expensive_order')
def most_expensive_order():
	data_loader = DataLoader()
	parser = Parser(data_loader.load_order_list())
	the_user_list = UserList(data_loader.load_user_list())
	most_expensive_order = parser.most_expensive_order()
	return 'Total price: ' + str(most_expensive_order.total_price()) + " ordered by: " + the_user_list.user_by_id(most_expensive_order.user_id)['username']

@app.route('/refresh')
def refresh():
    DataLoader().refresh_data()
    return 'Data refreshed'
