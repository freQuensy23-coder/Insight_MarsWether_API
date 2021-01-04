import unittest
from db import DB


class Tester(unittest.TestCase):
    def setUp(self) -> None:
        self.db = DB(file_name="test_data.sqlite")
        # TODO Add table creation and fake data generation
