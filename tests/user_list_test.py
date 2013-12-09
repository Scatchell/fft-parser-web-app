import unittest
import json
from src.user_list import UserList

class TestParser(unittest.TestCase):

    def setUp(self):
        users_json = '[{"id":26,"email":"rmatovu@thoughtworks.com","created_at":"2013-10-14T06:49:38.702Z","updated_at":"2013-10-14T06:49:38.735Z","username":"rmatovu","is_admin":false,"notifications":true},{"id":51,"email":"grao@thoughtworks.com","created_at":"2013-10-24T08:24:25.883Z","updated_at":"2013-10-24T08:24:25.900Z","username":"Gayathri Rao ","is_admin":false,"notifications":true},{"id":13,"email":"jcowie@thoughtworks.com","created_at":"2013-10-11T07:41:26.093Z","updated_at":"2013-10-11T07:41:26.185Z","username":"jcowie","is_admin":false,"notifications":true},{"id":28,"email":"wkinya@thoughtworks.com","created_at":"2013-10-14T07:12:14.883Z","updated_at":"2013-10-14T07:12:14.965Z","username":"wamboyee","is_admin":false,"notifications":true}]'
        self.users_list = UserList(users_json)

    def test_should_find_user_name_by_id(self):
    	queried_user = self.users_list.user_by_id(26)
        self.assertEqual(queried_user['id'], 26)
        self.assertEqual(queried_user['email'], 'rmatovu@thoughtworks.com')
        self.assertEqual(queried_user['username'], 'rmatovu')


if __name__ == '__main__':
    unittest.main()
