from music21 import *

class MusicInterpreter:

    def __init__(self) -> None:
        self.ensemble_song = {}
        self.streamer = stream.Stream()
        self.parts = []

    def interpret(self, ast):
        self.ensemble_song = ast

        self.streamer.insert(0, tempo.MetronomeMark(number=self.ensemble_song['Tempo']))
        self.streamer.append(meter.TimeSignature(f'{self.ensemble_song['Time Signature'][0]}/{self.ensemble_song['Time Signature'][1]}'))
        
        for line in self.ensemble_song['lines'].values():
            # print(line)
            p = stream.Part()
            for n in line:
                # print(n)
                if n[0] == '-' or n[0] == '--':
                    temp = note.Rest()
                else:
                    temp = note.Note(n[0])
                temp.duration.quarterLength = n[1]
                p.append(temp)
            self.parts.append(p)
            # print(self.parts)
        
        for part in self.parts:
            self.streamer.insert(0, part)
        
        # for item in self.streamer:
        #     print(item)
        print(f"Now playing {self.ensemble_song['Title']} ...")
        self.streamer.show('midi')




















        #        /\
        #        | \  
        #  ------|-/--------------
        #        |/   
        #  -----/|----------------
        #      / |  
        #  ---/-/|\---------------
        #    ( | | \
        #  ---\--|--)-------------
        #      \ | /
        #  -----\|/---------------
        #      @_|

        #  --_____________________
        #
        #

        # s = stream.Score()
        # parts = []

        # for item in ast:

        #     if item[0][:-1] == "part":

        #         p = stream.Part()

        #         for Note in item[1]:
        #             pitch = Note[0]
        #             length = Note[1]
                    
        #             if pitch == "hold":
        #                 p[-1].duration.quarterLength += 1.0
        #                 continue
        #             elif pitch == "rest":
        #                 curr_note = note.Rest()
        #             else:
        #                 curr_note = note.Note(pitch)

        #             curr_note.duration.quarterLength = length
        #             p.append(curr_note)
                
        #         parts.append(p)
        #         s.insert(0, p)

        # staff_group = layout.StaffGroup(parts,
        #     )
