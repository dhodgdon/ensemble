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
            "Token(type='TITLE', value='Title', lineno=2, index=13, end=18)",
            "Token(type='COLON', value=':', lineno=2, index=18, end=19)",
            "Token(type='STRING', value='\"My Song\"', lineno=2, index=20, end=29)",
            "Token(type='TEMPO', value='Tempo', lineno=3, index=42, end=47)",
            "Token(type='COLON', value=':', lineno=3, index=47, end=48)",
            "Token(type='TEMPO_NUM', value='100', lineno=3, index=49, end=52)",
            "Token(type='TIME_SIGNATURE', value='Time Signature', lineno=4, index=65, end=79)",
            "Token(type='COLON', value=':', lineno=4, index=79, end=80)",
            "Token(type='TS_NUM', value='4/4', lineno=4, index=81, end=84)",
            "Token(type='OPEN_BR', value='[', lineno=6, index=98, end=99)",
            "Token(type='NOTE', value='C4', lineno=6, index=100, end=102)",
            "Token(type='COMMA', value=',', lineno=6, index=102, end=103)",
            "Token(type='NOTE', value='D4', lineno=6, index=104, end=106)",
            "Token(type='COMMA', value=',', lineno=6, index=106, end=107)",
            "Token(type='NOTE', value='E4', lineno=6, index=108, end=110)",
            "Token(type='COMMA', value=',', lineno=6, index=110, end=111)",
            "Token(type='NOTE', value='C4', lineno=6, index=112, end=114)",
            "Token(type='CLOSE_BR', value=']', lineno=6, index=114, end=115)"]
            
        for token in test_tokens:
            self.assertEqual(token, f"{next(tokens)}")
            

    
    def test_invalid_input(self):
        lexer = MusicLexer()
        with self.assertRaises(ValueError):
            tokens = lexer.tokenize("""
            My Title Is "Hello World!"
            I want the tempo to be 100.
            """)
            for token in tokens:
                print(token)


if __name__ == '__main__':
    unittest.main()