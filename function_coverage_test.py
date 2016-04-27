import unittest
from Model import *

class FunctionCoverageTests(unittest.TestCase):

    def setUp(self):
        self.model = Model()

    def tearDown(self):
        print("next")

    def test_read_in_csv(self):
        self.model.read_in_csv("testFileLoad.txt")
        self.expected = ['Hello This Is A Test', 'Hello This is Another Test']
        self.actual = self.model.get_data_set()
        self.assertTrue(self.expected == self.actual)

    def test_get_data(self):
        self.model.read_in_csv("TestData.csv")
        self.expected = 0
        self.actual = self.model.get_data().__len__()
        self.assertTrue(self.expected == self.actual)

    def test_wash_data(self):
        self.model.read_in_csv("TestData.csv")
        self.expected = 7
        self.actual = self.model.wash_data().__len__()
        self.assertTrue(self.expected == self.actual)


if __name__ == "__main__":
    unittest.main(verbosity=2)