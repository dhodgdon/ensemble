from sly import Parser
from ens_lexer import MusicLexer

class MusicParser(Parser):
    tokens = MusicLexer.tokens

    def __init__(self):
        self.tokens = MusicLexer.tokens
        self.current_part = []
    
    @_('line')
    def harmony(self, p):
        notes = []
        for note in p.line:
            notes.append([note])
        return notes
    
    @_('OPEN_BR part CLOSE_BR')
    def line(self, p):
        return p.part


    # @_('line line')
    # def harmony(self, p):
    #     if len(p.line0) != len(p.line1):
    #         raise ValueError(f"Number of notes per line must match")
        
    #     chords = []

    #     i = 0
    #     while i < len(p.line0):
    #         notes_in_chord = []
    #         notes_in_chord.append(p.line0[i])
    #         notes_in_chord.append(p.line1[i])
    #         chords.append(notes_in_chord)
    #         i += 1

    #     return chords
    
    @_('harmony line')
    def harmony(self, p):
        # if len(p.harmony) % len(p.line) != 0:
        if len(p.harmony) != len(p.line):
            raise ValueError(f"Number of notes per line must match")
        
        i = 0
        for chord in p.harmony:
            chord.append(p.line[i])
            i += 1

        return p.harmony
    




    #######################################
    # Ideas for expansion:
    #######################################
    
    # (line line) -> harmony
    # (line) -> piece
    # (piece line) -> piece

    # Have an .opus file with multiple .ens files named in it,
    # each with different instruments, to play an orchestra.
    # (piece piece) -> opus
    # (opus piece) -> opus

    #######################################
    #######################################

    # @_('TITLE COLON STRING')
    # def part(self, p):
    #     return ('TITLE', p.TITLE)

    # @_('TEMPO COLON INT')
    # def part(self, p):
    #     return ('TEMPO', p.TEMPO)

    # @_('TIME_SIGNATURE COLON NUMERATOR SLASH DENOMINATOR')
    # def part(self, p):
    #     return ('TIME_SIGNATURE', p.TIME_SIGNATURE)

    # @_('part LINE part')
    # def part(self, p):
    #     return p.part0 + p.part1

    # @_('STRING')
    # def title(self, p):
    #     return p.STRING[1:-1]

    # @_('INT')
    # def tempo(self, p):
    #     return int(p.INT)

    # @_('NUMERATOR SLASH DENOMINATOR')
    # def time_signature(self, p):
    #     return f"{p.NUMERATOR}/{p.DENOMINATOR}"

    # @_('part')
    # def part(self, p):
    #     return p.part

    @_('NOTE')
    def note_rest_hold(self, p):
        return p.NOTE

    @_('REST')
    def note_rest_hold(self, p):
        return p.REST
    
    @_('HOLD')
    def note_rest_hold(self, p):
        return p.HOLD

    # @_('note_rest_hold HOLD')
    # def note_rest_hold(self, p):
    #     return (p.note_rest_hold, p.HOLD)

    # @_('note_rest_hold COMMA note_rest_hold COMMA note_rest_hold')
    # def note_sequence(self, p):
    #     return [p.note_rest_hold0, p.note_rest_hold1, p.note_rest_hold2]

    @_('note_rest_hold COMMA note_rest_hold COMMA note_rest_hold COMMA note_rest_hold')
    def measure(self, p):
        return [p.note_rest_hold0, p.note_rest_hold1, p.note_rest_hold2, p.note_rest_hold3]

    # @_('measure BAR measure')
    # def part(self, p):
    #     return [p.measure0[0][0], p.measure1[0][0]]

    @_('measure')
    def part(self, p):
        return p.measure

    @_('part BAR measure')
    def part(self, p):
        return p.part + p.measure

    # @_('measure BAR measure')
    # def part(self, p):
    #     return p.measure0 + p.measure1



    # @_('bar BAR bar')
    # def bar_bar(self, p):
    #     return p.bar0 + p.bar1

    # @_('bar_bar LINE bar_bar')
    # def bar_bar(self, p):
    #     return p.bar_bar0 + p.bar_bar1


# class MusicParser(Parser):

#     def __init__(self):
#         # self.tokens = tokens
#         self.current_part = []
    
#     @_('line line')
#     def harmony(self, p):
#         if len(p.line0) != len(p.line1):
#             raise ValueError(f"Number of notes per line must match")
        
#         chords = []

#         i = 0
#         while i < len(p.line0):
#             notes_in_chord = []
#             notes_in_chord.append(p.line0[i])
#             notes_in_chord.append(p.line1[i])
#             chords.append(notes_in_chord)
#             i += 1

#         return chords
    
#     @_('harmony line')
#     def harmony(self, p):
#         # if len(p.harmony) % len(p.line) != 0:
#         if len(p.harmony) != len(p.line):
#             raise ValueError(f"Number of notes per line must match")
        
#         i = 0
#         for chord in p.harmony:
#             chord.append(p.line[i])
#             i += 1

#         return p.harmony
    
#     @_('OPEN_BR part CLOSE_BR')
#     def line(self, p):
#         return p.part



#     #######################################
#     # Ideas for expansion:
#     #######################################
    
#     # (line line) -> harmony
#     # (line) -> piece
#     # (piece line) -> piece

#     # Have an .opus file with multiple .ens files named in it,
#     # each with different instruments, to play an orchestra.
#     # (piece piece) -> opus
#     # (opus piece) -> opus

#     #######################################
#     #######################################

#     # @_('TITLE COLON STRING')
#     # def part(self, p):
#     #     return ('TITLE', p.TITLE)

#     # @_('TEMPO COLON INT')
#     # def part(self, p):
#     #     return ('TEMPO', p.TEMPO)

#     # @_('TIME_SIGNATURE COLON NUMERATOR SLASH DENOMINATOR')
#     # def part(self, p):
#     #     return ('TIME_SIGNATURE', p.TIME_SIGNATURE)

#     # @_('part LINE part')
#     # def part(self, p):
#     #     return p.part0 + p.part1

#     # @_('STRING')
#     # def title(self, p):
#     #     return p.STRING[1:-1]

#     # @_('INT')
#     # def tempo(self, p):
#     #     return int(p.INT)

#     # @_('NUMERATOR SLASH DENOMINATOR')
#     # def time_signature(self, p):
#     #     return f"{p.NUMERATOR}/{p.DENOMINATOR}"

#     @_('NOTE')
#     def note_rest_hold(self, p):
#         return p.NOTE

#     @_('REST')
#     def note_rest_hold(self, p):
#         return p.REST
    
#     @_('HOLD')
#     def note_rest_hold(self, p):
#         return p.HOLD

#     @_('note_rest_hold COMMA note_rest_hold COMMA note_rest_hold COMMA note_rest_hold')
#     def measure(self, p):
#         return [p.note_rest_hold0, p.note_rest_hold1, p.note_rest_hold2, p.note_rest_hold3]

#     @_('measure')
#     def part(self, p):
#         return p.measure

#     @_('part BAR measure')
#     def part(self, p):
#         return p.part + p.measure