class Item:
    def __init__(self, item_dict):
        self.id = item_dict['id']
        self.name = item_dict['name']
        self.price = item_dict['price']
        self.available = item_dict['available']