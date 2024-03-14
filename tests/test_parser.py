from sly import Parser
from test_lexer import MusicLexer
from functools import reduce

class MusicParser(Parser):
    tokens = MusicLexer.tokens

    def __init__(self):
        self.tokens = MusicLexer.tokens
        self.part_no = 1
        self.note_length = 1.0
        self.ensemble_song = {}
        self.ts_numerator = 0
        self.ts_denominator = 0

    @_('title tempo time_signature line')
    def song(self, p):
        self.ensemble_song["lines"] = {f"line{self.part_no}" : p.line}
        self.part_no += 1
        return self.ensemble_song

    @_('OPEN_BR notes CLOSE_BR')
    def line(self, p):
        return p.notes

    @_('song line')
    def song(self, p):
        self.ensemble_song["lines"][f"line{self.part_no}"] = p.line
        self.part_no += 1
        return self.ensemble_song


    @_('TITLE COLON STRING')
    def title(self, p):
        self.ensemble_song[p.TITLE] = p.STRING
        # return (p.TITLE, p.STRING)

    @_('TEMPO COLON TEMPO_NUM') # The default tempo for a stream.Stream() object is 120 (quarter notes per minute).
    def tempo(self, p):
        self.ensemble_song[p.TEMPO] = int(p.TEMPO_NUM)
        # return (p.TEMPO, p.TEMPO_NUM)

    @_('TIME_SIGNATURE COLON TS_NUM')
    def time_signature(self, p):
        self.ts_numerator = int(p.TS_NUM[0])
        # print(self.ts_numerator)
        self.ts_denominator = int(p.TS_NUM[2])
        self.note_length = 4.0 / int(p.TS_NUM[2])
        self.ensemble_song[p.TIME_SIGNATURE] = (self.ts_numerator, self.ts_denominator)
        # return (p.TIME_SIGNATURE, p.TS_NUM[0], p.TS_NUM[2])

    # @_('title tempo time_signature')
    # def song_metadata(self, p):
    #     self.ensemble_song[]


    # @_('OPEN_BR part CLOSE_BR')
    # def line(self, p):
    #     return p.part




    @_('NOTE')
    def note_rest(self, p):
        return (p.NOTE, self.note_length)

    @_('REST')
    def note_rest(self, p):
        return (p.REST, self.note_length)


    # @_('line')
    # def harmony(self, p):
    #     notes = []
    #     for note in p.line:
    #         notes.append([note])
    #     print(p.line)
    #     self.part_no += 1
    #     return [(f"part{self.part_no}", p.line[1][0])]

    # @_('line')
    # def harmony(self, p):
    #     pass




    # @_('harmony line')
    # def harmony(self, p):
    #     if len(p.harmony) % len(p.line) != 0:
    #     if len(p.harmony[0][1]) != len(p.line):
    #         raise ValueError(f"Number of notes per line must match")

    #     i = 0
    #     for chord in p.harmony:
    #         chord.append(p.line[i])
    #         i += 1

    #     self.part_no += 1
    #     p.harmony.append((f"part{self.part_no}", p.line))


    #     return p.harmony

    # @_('time_signature harmony')
    # def song(self, p):
    #     return (p.time_signature, p.harmony)

    # @_('time_signature')

    # @_('TIME_SIGNATURE COLON NUM')
    # def time_signature(self, p):
    #     print("time signature")
    #     return ('TIME_SIGNATURE', int(p.NUM[0]), int(p.NUM[2]))
    #     return ('TIME_SIGNATURE', f"{p.NUMERATOR}", f"{p.DENOMINATOR}")


    # @_('time_signature OPEN_BR part CLOSE_BR')
    # def line(self, p):
    #     return (p.time_signature, ("parts", p.part))

    # @_('time_signature OPEN_BR part CLOSE_BR')
    # def line(self, p):
    #     return (p.time_signature, ("parts", p.part))



    # @_('note_rest COMMA HOLD')
    # def note_rest(self, p): # edit this?
    #     # p.note_rest[1] += 1.0
    #     return (p.note_rest[0], p.note_rest[1] + 1.0)

    # These are the first two notes of the line.
    @_('note_rest COMMA note_rest')
    def notes(self, p):
        # print([p.note_rest0, p.note_rest1])
        return [p.note_rest0, p.note_rest1]
    
    # This case only happens when the first note 
    # is immediately followed by a hold.
    @_('note_rest COMMA HOLD')
    def notes(self, p):
        return [(p.note_rest[0], p.note_rest[1] + self.note_length)]
    
    # @_('note_rest NOTE_DIV')
    # def note_rest(self, p):
    #     index = 1
    #     # while type(p.NOTE_DIV[index]) != int:
    #     #     index += 1
    #     while True:
    #         if index > len(p.NOTE_DIV) - 1:
    #             raise IndexError("Cannot have more than one space between / and number.")
    #         try:
    #             int(p.NOTE_DIV[index])
    #             break
    #         except ValueError:
    #             index += 1
    #             continue
    #     return [(p.note_rest[0], p.note_rest[1] / float(p.NOTE_DIV[index:]))]

    @_('notes COMMA note_rest')
    def notes(self, p):
        p.notes.append(p.note_rest)
        # print(p.notes)
        return p.notes

    @_('notes COMMA HOLD')
    def notes(self, p):
        p.notes[-1] = (p.notes[-1][0], p.notes[-1][1] + self.note_length)
        # print(p.notes)
        return p.notes

    # @_('notes BAR note_rest')
    @_('notes BAR note_rest', 'notes BAR HOLD')
    def notes(self, p):
        # Check that the total length of the notes
        # is equal to the numerator.
        # if so, self.measure_count += 1
        total_notes_length = reduce(lambda x, y: x + y[1], p.notes, 0)
        print(total_notes_length % (self.ts_numerator / (self.ts_denominator / 4.0)))
        if total_notes_length % (self.ts_numerator / (self.ts_denominator / 4.0)) == 0:
            if p[2] == '~' or p[2] == '~~':
                p.notes[-1] = (p.notes[-1][0], p.notes[-1][1] + self.note_length)
            else:
                p.notes.append(p[2])
            # print(p.notes)
            return p.notes
        else:
            raise ValueError(f"Number of notes per measure must match time signature.")



    # @_('note_rest COMMA note_rest COMMA note_rest COMMA note_rest')
    # def measure(self, p):
    #     return [p.note_rest0, p.note_rest1, p.note_rest2, p.note_rest3]

    # @_('measure')
    # def part(self, p):
    #     return p.measure

    # @_('part BAR measure')
    # def part(self, p):
    #     print("something")
    #     return p.part + p.measure



    #######################################
    # Ideas for expansion:
    #######################################

    # Have an .opus file with multiple .ens files named in it,
    # each with different instruments, to play an orchestra.
    # (piece piece) -> opus
    # (opus piece) -> opus

    #######################################
    #######################################