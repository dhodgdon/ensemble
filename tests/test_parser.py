import unittest
from ensemble.ens_parser import MusicParser

class TestParser(unittest.TestCase):
    def test_parsing(self):
        parser = MusicParser()
        ast = parser.parse("<put tokenized tokens here>")
        self.assertEqual(ast, "<put expected output here>")
    
    def test_invalid_syntax(self):
        parser = MusicParser()
        with self.assertRaises(Exception):
            ast = parser.parse("<put invalid token here>")


if __name__ == '__main__':
    unittest.main()