import unittest
from main import hello_world, greet_person

class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello, Git World!")
    def test_greet_person(self):
        self.assertEqual(greet_person("Alice"), "Hello, Alice!")

if __name__ == '__main__':
    unittest.main()