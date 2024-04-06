# AI assisted in the creation of this code.

import unittest
from ensemble.ens_parser import MusicParser
from ensemble.ens_lexer import MusicLexer

class TestParser(unittest.TestCase):
    def test_parsing(self):
        lexer = MusicLexer()
        tokens = lexer.tokenize('''
            Title: "My Song"
            Tempo: 100
            Time Signature: 4/4

            [ C4, D4, E4, C4]
            
            ''')
        parser = MusicParser()
        ast = parser.parse(tokens)
        self.assertEqual(f"{ast}", "{'Title': '\"My Song\"', 'Tempo': 100, 'Time Signature': (4, 4), 'lines': {'line1': [('C4', 1.0), ('D4', 1.0), ('E4', 1.0), ('C4', 1.0)]}}")
    
    def test_invalid_syntax(self):
        parser = MusicParser()
        with self.assertRaises(Exception):
            parser.parse("Invalid tokens here")

    def test_incorrect_number_of_notes(self):
        test_text1 = '''

        Title: "My Song"
        Tempo: 100
        Time Signature: 4/4

        [ C4, D4, E4, C4 | D4, E4, C4 ]

        '''
        test_text2 = '''

        Title: "My Song"
        Tempo: 100
        Time Signature: 4/4

        [ C4, D4, E4, C4 | D4, E4, C4 | C4, D4, E4, C4 ]

        '''
        test_tokens1 = MusicLexer().tokenize(test_text1)
        test_tokens2 = MusicLexer().tokenize(test_text2)
        parser = MusicParser()
        
        with self.assertRaises(ValueError):
            parser.parse(test_tokens1)

        with self.assertRaises(ValueError):
            parser.parse(test_tokens2)


if __name__ == '__main__':
    unittest.main()