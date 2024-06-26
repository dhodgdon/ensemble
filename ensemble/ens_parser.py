# AI assisted in the creation of this code.

from sly import Parser
from .ens_lexer import MusicLexer
from functools import reduce
import math

class MusicParser(Parser):
    tokens = MusicLexer.tokens

    def __init__(self):
        self.tokens = MusicLexer.tokens
        self.part_no = 1
        self.note_length = 1.0
        self.ensemble_song = {}
        self.ts_numerator = 0
        self.ts_denominator = 0
        self.transpose_amount = 0

    @_('title tempo time_signature opt_transpose line')
    def song(self, p):
        self.ensemble_song["lines"] = {f"line{self.part_no}" : p.line}
        self.part_no += 1
        return self.ensemble_song

    @_('OPEN_BR notes CLOSE_BR')
    def line(self, p):
        if self.has_correct_length(p):
            return p.notes

    @_('song line')
    def song(self, p):
        self.ensemble_song["lines"][f"line{self.part_no}"] = p.line
        self.part_no += 1
        return self.ensemble_song


    @_('TITLE COLON STRING')
    def title(self, p):
        self.ensemble_song[p.TITLE] = p.STRING

    # Tempo always refer to quarter note beats per minutes.
    @_('TEMPO COLON TEMPO_NUM') # The default tempo for a stream.Stream() object is 120 (quarter notes per minute).
    def tempo(self, p):
        self.ensemble_song[p.TEMPO] = int(p.TEMPO_NUM)

    @_('TIME_SIGNATURE COLON TS_NUM')
    def time_signature(self, p):
        self.ts_numerator = int(p.TS_NUM[0])
        self.ts_denominator = int(p.TS_NUM[2])
        
        # This calculates how long each note should last.
        # Quarter notes last 1.0, so we divide 4.0 (or four
        # quarter notes) by the denominator of the time
        # signature. For example, 6/8 time would yield 
        # 4.0/8, which simplifies to 0.5; and eighth notes
        # are indeed half of a quarter note.
        self.note_length = 4.0 / self.ts_denominator
        self.ensemble_song[p.TIME_SIGNATURE] = (self.ts_numerator, self.ts_denominator)


    @_('empty')
    def opt_transpose(self, p):
        return p.empty

    @_('transpose')
    def opt_transpose(self, p):
        return p.transpose

    @_('TRANSPOSE COLON TR_NUM') # FIX THIS FUNCTION
    def transpose(self, p):
        if p.TR_NUM[0] == "+":
            inted = int(p.TR_NUM[1:])
        else:
            inted = int(p.TR_NUM)

        self.transpose_amount = inted
        self.ensemble_song[p.TRANSPOSE] = inted

        # self.transpose_amount = int(p.TR_NUM[1:])
        # self.ensemble_song[p.TRANSPOSE] = int(p.TR_NUM[1:])

    @_('')
    def empty(self, p):
        pass

    @_('NOTE')
    def note_rest(self, p):
        return (p.NOTE, self.note_length)

    @_('REST')
    def note_rest(self, p):
        return (p.REST, self.note_length)
    
    # ----------------------------------------
    @_('note_rest FRACTION')
    def note_rest(self, p):
        return (p.note_rest[0], p.note_rest[1] / int(p.FRACTION[1:]))
    # ----------------------------------------

    # These are the first two notes of the line.
    @_('note_rest COMMA note_rest')
    def notes(self, p):
        return [p.note_rest0, p.note_rest1]
    
    # This case only happens when the first note 
    # is immediately followed by a hold.
    @_('note_rest COMMA HOLD')
    def notes(self, p):
        return [(p.note_rest[0], p.note_rest[1] + self.note_length)]

    @_('notes COMMA note_rest')
    def notes(self, p):
        p.notes.append(p.note_rest)
        return p.notes

    @_('notes COMMA HOLD')
    def notes(self, p):
        p.notes[-1] = (p.notes[-1][0], p.notes[-1][1] + self.note_length)
        return p.notes
    
    @_('notes BAR note_rest', 'notes BAR HOLD')
    def notes(self, p):
        if self.has_correct_length(p):
            if p[2] == '~' or p[2] == '~~':
                p.notes[-1] = (p.notes[-1][0], p.notes[-1][1] + self.note_length)
            else:
                p.notes.append(p[2])
            return p.notes
        
    def has_correct_length(self, p):
        total_notes_length = reduce(lambda x, y: x + y[1], p.notes, 0)
        
        # Below, we calculate if the length of each measure is correct according to our 
        # specified time signature. We first divide the denominator of the time 
        # signature by 4.0 to determine how many of each note will make up a quarter 
        # note. For instance, with 9/12 time 12/4.0 = 3, so it takes 3 notes to make a 
        # quarter note beat. We then divide the numerator by this number to determine 
        # how many quarter notes should be in each measure. Again using the 9/12 time 
        # signature example, this would give us 9/3 = 3, which is correct. Finally, we 
        # modularly divide the length of all the notes in this line of music by that 
        # number to confirm that each measure is indeed the correct length. Because we 
        # perform this calculation at each measure, all the measures will have the 
        # correct length.
        if total_notes_length % (self.ts_numerator / (self.ts_denominator / 4.0)) == 0:
            return True
        else:
            incorrect_measure = math.ceil(total_notes_length / (self.ts_numerator / (self.ts_denominator / 4.0)))
            raise ValueError(f"Incorrect number of beats in measure {incorrect_measure}. Number of beats per measure must match time signature.")


    #######################################
    # Ideas for expansion:
    #######################################

    # Have an .opus file with multiple .ens files named in it,
    # each with different instruments, to play an orchestra.
    # (piece piece) -> opus
    # (opus piece) -> opus

    #######################################
    #######################################