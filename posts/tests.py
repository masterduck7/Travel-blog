from django.test import TestCase


class ApiTests(TestCase):
    def test_init(self):
        test = False
        self.assertIs(test, False)
