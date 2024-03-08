from music21 import *

class Interpreter:

    def __init__(self) -> None:
        pass

    def interpret(self, ast) -> None:
        music_stream = stream.Stream()

        for curr_chord in ast:
            # Currently working:
            curr_chord = [x for x in curr_chord if x not in ['-', '--', '~', '~~']]
            # print(curr_chord)

            # Not yet working:
            # curr_chord = [x for x in curr_chord if x not in ['-', '--']]
            # # hold_indices = [index for index, value in enumerate(curr_chord) if value in ['~', '~~']]
            # # print(hold_indices)
            # i = -1
            # hold_length = 1.0
            # if len(music_stream) > 1 and music_stream[i] in ['~', '~~']:
            #     while music_stream[i] in ['~', '~~']:
            #         i -= 1
            #         hold_length += 1.0

            #     music_stream[i].duration.quarterLength = hold_length

            music_stream.append(chord.Chord(curr_chord))

        print(music_stream[-1])
        music_stream.show('midi')