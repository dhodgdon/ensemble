from sly import Lexer

class MusicLexer(Lexer):
    tokens = {
            #   TITLE, TEMPO, TIME_SIGNATURE, COLON, 
                OPEN_BR, CLOSE_BR, COMMA, BAR, NOTE, REST, HOLD
                # , 
            #   PART, LINE, 
            #   STRING, INT, NUMERATOR, SLASH, DENOMINATOR
              }
    
    # Tokens
    # TITLE = r'Title'
    # TEMPO = r'Tempo'
    # TIME_SIGNATURE = r'Time Signature'
    # COLON = r':'
    OPEN_BR = r'\['
    CLOSE_BR = r'\]'
    COMMA = r','
    BAR = r'\|'
    # REST = r'\-'
    # HOLD = r'\~'
    REST = r'--?'
    HOLD = r'~~?'
    # PART = r'\n'
    # LINE = r'\n\n'
    # STRING = r'"[^"]*"'
    # INT = r'\d+'
    # NUMERATOR = r'\d+'
    # SLASH = r'/'
    # DENOMINATOR = r'\d+'

    # Note token
    @_(r'[A-Ga-g][0-9][b#n]?')
    def NOTE(self, t):
        return t
    
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += len(t.value)

    # Ignore whitespace
    ignore = ' \t\f\r\v'

    def error(self, t):
        raise ValueError(f"Illegal character '{t.value[0]}' at line {t.lineno}")
