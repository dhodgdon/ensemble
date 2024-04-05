# AI assisted in the creation of this code.

import unittest
from ensemble.ens_lexer import MusicLexer

class TestLexer(unittest.TestCase):
    def test_tokenization(self):
        lexer = MusicLexer()
        tokens = lexer.tokenize('''
        Title: "My Song"
        Tempo: 100
        Time Signature: 4/4

            [ C4, D4, E4, C4]
            
        ''')

        test_tokens = [
            Token(type='TITLE', value='Title', lineno=3, index=2, end=7)
    Token(type='COLON', value=':', lineno=3, index=7, end=8)
    Token(type='STRING', value='"My Song"', lineno=3, index=9, end=18)
    Token(type='TEMPO', value='Tempo', lineno=4, index=19, end=24)
    Token(type='COLON', value=':', lineno=4, index=24, end=25)
    Token(type='TEMPO_NUM', value='100', lineno=4, index=26, end=29)
    Token(type='TIME_SIGNATURE', value='Time Signature', lineno=5, index=30, end=44)
    Token(type='COLON', value=':', lineno=5, index=44, end=45)
    Token(type='TS_NUM', value='4/4', lineno=5, index=46, end=49)
    Token(type='OPEN_BR', value='[', lineno=7, index=55, end=56)
    Token(type='NOTE', value='C4', lineno=7, index=57, end=59)
    Token(type='COMMA', value=',', lineno=7, index=59, end=60)
    Token(type='NOTE', value='D4', lineno=7, index=61, end=63)
    Token(type='COMMA', value=',', lineno=7, index=63, end=64)
    Token(type='NOTE', value='E4', lineno=7, index=65, end=67)
    Token(type='COMMA', value=',', lineno=7, index=67, end=68)
    Token(type='NOTE', value='C4', lineno=7, index=69, end=71)
    Token(type='CLOSE_BR', value=']', lineno=7, index=71, end=72)]
            
    counter = 0
    for token in tokens:
        self.assertEqual(token, [Token(type='TITLE', value='Title', lineno=3, index=2, end=7)
    Token(type='COLON', value=':', lineno=3, index=7, end=8)
    Token(type='STRING', value='"My Song"', lineno=3, index=9, end=18)
    Token(type='TEMPO', value='Tempo', lineno=4, index=19, end=24)
    Token(type='COLON', value=':', lineno=4, index=24, end=25)
    Token(type='TEMPO_NUM', value='100', lineno=4, index=26, end=29)
    Token(type='TIME_SIGNATURE', value='Time Signature', lineno=5, index=30, end=44)
    Token(type='COLON', value=':', lineno=5, index=44, end=45)
    Token(type='TS_NUM', value='4/4', lineno=5, index=46, end=49)
    Token(type='OPEN_BR', value='[', lineno=7, index=55, end=56)
    Token(type='NOTE', value='C4', lineno=7, index=57, end=59)
    Token(type='COMMA', value=',', lineno=7, index=59, end=60)
    Token(type='NOTE', value='D4', lineno=7, index=61, end=63)
    Token(type='COMMA', value=',', lineno=7, index=63, end=64)
    Token(type='NOTE', value='E4', lineno=7, index=65, end=67)
    Token(type='COMMA', value=',', lineno=7, index=67, end=68)
    Token(type='NOTE', value='C4', lineno=7, index=69, end=71)
    Token(type='CLOSE_BR', value=']', lineno=7, index=71, end=72)])
    
    def test_invalid_input(self):
        lexer = MusicLexer()
        with self.assertRaises(Exception):
            tokens = lexer.tokenize("<put invalid input here>")


if __name__ == '__main__':
    unittest.main()