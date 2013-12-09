import json

class UserList:
	def __init__(self, users_list):
		self.user_list = users_list

	def user_by_id(self, user_id):
		for user in self.user_list:
			if user['id'] == user_id:
				return user

