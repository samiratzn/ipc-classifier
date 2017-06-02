"""Unitary tests to test functions in the most compact way possible"""
import unittest
from tests import factories
from classifier import preprocessing_tools as utils

class TestPreprocessingTools(unittest.TestCase):
    """Test methods from the preprocessing tools package"""
    def setUp(self):
        self.classifier = factories.PatentModelFactory()
        with open("tests/data/patent.xml", 'r') as file_patent:
            self.text_patent = file_patent.read()

    def test_fields_extraction(self):
        """Verify if the main code and the list of secondary codes are correct"""
        codes = utils._extract_fields(self.text_patent)
        self.assertEqual(self.classifier.ipcs, codes.ipcs)
        self.assertEqual(self.classifier.list_ipc, codes.list_ipc)
        self.assertEqual(self.classifier.number, codes.number)
        self.assertEqual(self.classifier.abstract, codes.abstract)
        
if __name__ == '__main__':
    unittest.main()
