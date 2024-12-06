import unittest

class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        if user not in self.users:
            self.users.append(user)
        else:
            return "User already exists"  # OK

    def remove_user(self, user):
       # self.users.remove(user)  acusa erro caso o usuário a ser removido não esteja na lista.
        if user in self.users: # verifica se o usuário existe antes de remover.
            self.users.remove(user)
        else:
            return "User not found"

class TestUserManager(unittest.TestCase):
    def setUp(self):
        self.manager = UserManager()

    def test_add_user(self):
        self.manager.add_user("Daniel")
        self.assertIn("Daniel", self.manager.users)

    def test_add_duplicate_user(self):
        self.manager.add_user("Daniel")
        result = self.manager.add_user("Daniel")
        self.assertEqual(result, "User already exists")

    def test_remove_user(self):
        self.manager.add_user("Daniel")
        self.manager.remove_user("Daniel")
        self.assertNotIn("Daniel", self.manager.users)

    def test_remove_nonexistent_user(self):
        result = self.manager.remove_user("Sidney")
        self.assertEqual(result, "User not found")

if __name__ == "__main__":
    unittest.main()
