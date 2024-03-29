from sly import Lexer

class MusicLexer(Lexer):
    tokens = {
                TITLE, 
                TEMPO, 
                TIME_SIGNATURE, 
                TRANSPOSE,
                COLON, 
                OPEN_BR, 
                CLOSE_BR, 
                COMMA, 
                BAR, 
                NOTE, 
                REST, 
                HOLD, 
                TS_NUM, 
                TEMPO_NUM, 
                TR_NUM,
                STRING,
                FRACTION
              }
    
    # Tokens
    TITLE = r'Title'
    TEMPO = r'Tempo'
    TIME_SIGNATURE = r'Time Signature'
    TRANSPOSE = r'Transpose'
    COLON = r':'
    OPEN_BR = r'\['
    CLOSE_BR = r'\]'
    COMMA = r','
    BAR = r'\|'
    # REST = r'--?'
    # HOLD = r'~~?'    
    REST = r'--'
    HOLD = r'~~'
    STRING = r'"[^"]*"'
    FRACTION = r'\/\d+'

    # FIX THESE NUMBERS TO ALL MATCH AND THEN DO RANGE CHECKING IN PARSER?
    TS_NUM = r'(2[0-1]|1[0-9]|[2-9])\/(3[0-2]|[1-2][0-9]|[2-9])'
    # TS_NUM = r'(1[0-2]|[2-9])\/(1[0-2]|[2-9])'
    TEMPO_NUM = r'\b(?:[1-9]|[1-9][0-9]|1[0-9]{2}|2[0-3][0-9]|240)\b'
    TR_NUM = r'(?:\+|-)(?:50|[0-4]?[0-9])'

    # Note token
    @_(r'[A-Ga-g][0-9][-#n]?')
    def NOTE(self, t):
        return t
    
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += len(t.value)

    # Ignore whitespace
    ignore = ' \t\f\r\v'

    ignore_comment = r'\#.*'

    def error(self, t):
        raise ValueError(f"Illegal character '{t.value[0]}' at line {t.lineno}")
