import unittest
from app import App

# test here
"""
person_information(dict)
normal: {name->string, phone_number -> number}
boundaries: {name -> "", "   ", 0777: phone_number -> [0, string, empty, -1, ]}
edge: {name -> "too long ", }
unexpected: {dict, list, file, }
"""

class AddContactTestCase(unittest.TestCase):
    def test_name_is_not_empty_string(self):
        app = App()
        result = app.do_add_contact("'' '' 0742534524")
        self.assertEqual(result, "Error firstname can not be empty")

    def test_phone_number_is_int(self):
        app = App()
        results = app.do_add_contact("Georgreen Mamboleo '030030423043'")
        self.assertEqual(results, "Error phone number cannot be int.")

    def test_unexpected_input(self):
        app = App()
        results = app.do_add_contact("[]")
        self.assertEqual(results, "Error unexpected input.")


if __name__ == '__main__':
    unittest.main()
