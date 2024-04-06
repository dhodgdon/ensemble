# AI assisted in the creation of this code.

import unittest
from ensemble.ens_interpreter import MusicInterpreter

class TestInterpreter(unittest.TestCase):
    def test_song_contents(self):
        interpreter = MusicInterpreter()

        interpreter.interpret({'Title': '"My Song"', 'Tempo': 100, 'Time Signature': (4, 4), 'lines': {'line1': [('C4', 1.0), ('D4', 1.0), ('E4', 1.0), ('C4', 1.0), ('D4', 1.0), ('E4', 1.0), ('C4', 1.0), ('D4', 1.0)]}}, execute=False)
        expected_notes = ["<music21.note.Note C>",
                          "<music21.note.Note D>",
                          "<music21.note.Note E>",
                          "<music21.note.Note C>",
                          "<music21.note.Note D>",
                          "<music21.note.Note E>",
                          "<music21.note.Note C>",
                          "<music21.note.Note D>"]
        expected_tempo = "<music21.tempo.MetronomeMark Quarter=100>"
        expected_time_sig = "<music21.meter.TimeSignature 4/4>"
        
        
        curr_index = 0
        while curr_index < len(expected_notes):
            self.assertEqual(expected_notes[curr_index], f"{interpreter.streamer[0][curr_index]}")
            curr_index += 1

        self.assertEqual(expected_tempo, f"{interpreter.streamer[1]}")
        self.assertEqual(expected_time_sig, f"{interpreter.streamer[2]}")

if __name__ == '__main__':
    unittest.main()