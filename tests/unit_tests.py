"""Unitary tests to test functions in the most compact way possible"""
import unittest
from tests import factories
from classifier import preprocessing_tools as utils

class TestPreprocessingTools(unittest.TestCase):
    """Test methods from the preprocessing tools package"""
    def setUp(self):
        self.patent = factories.PatentModelFactory()
        with open("tests/data/patent.xml", 'r') as file_patent:
            self.text_patent = file_patent.read()
        self.text_words = ("dog no cat yes may internet book page internet dog great")
        self.list_words = set(["dog", "cat", "internet", "book", "page", "great", "yes", "may"])
        self.list_plurals = ['caresses', 'flies', 'dies', 'mules', 'denied',
                             'died', 'agreed', 'owned', 'humbled', 'sized',
                             'meeting', 'stating', 'siezing', 'itemization',
                             'sensational', 'traditional', 'reference', 'colonizer',
                             'plotted']
        self.list_singles = ["caress", "fli", "die", "mule", "deni", "die", "agre", "own", "humbl",
                             "size", "meet", "state", "siez", "item", "sensat", "tradit", "refer",
                             "colon", "plot"]


    def test_fields_extraction(self):
        """Verify if the main code and the list of secondary codes are correct"""
        patent = utils._extract_fields(self.text_patent)
        self.assertEqual(self.patent.ipcs, patent.ipcs)
        self.assertEqual(self.patent.list_ipc, patent.list_ipc)
        self.assertEqual(self.patent.number, patent.number)
        self.assertEqual(self.patent.abstract, patent.abstract)
        self.assertEqual(self.patent.title, patent.title)

    def test_words_extraction(self):
        """Verify if the extraction of words from the abstract works right"""
        list_words = utils._extract_word_list(self.text_words)
        self.assertEqual(self.list_words, list_words)

    def test_stemming(self):
        """Verify the stemming process' output"""
        self.assertEqual(self.list_singles, utils._stem_words_list(self.list_plurals))

if __name__ == '__main__':
    unittest.main()
