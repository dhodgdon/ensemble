# AI assisted in the creation of this code.

from music21 import *

class MusicInterpreter:

    def __init__(self) -> None:
        self.ensemble_song = {}
        self.streamer = stream.Stream()
        self.parts = []

    def interpret(self, ast):
        self.ensemble_song = ast

        self.streamer.insert(0, tempo.MetronomeMark(number=self.ensemble_song['Tempo']))
        self.streamer.append(meter.TimeSignature(f"{self.ensemble_song['Time Signature'][0]}/{self.ensemble_song['Time Signature'][1]}"))
        
        for line in self.ensemble_song['lines'].values():
            p = stream.Part()
            for n in line:
                if n[0] == '-' or n[0] == '--':
                    temp = note.Rest()
                else:
                    temp = note.Note(n[0])
                temp.duration.quarterLength = n[1]
                p.append(temp)
            self.parts.append(p)
        
        for part in self.parts:
            self.streamer.insert(0, part)
            
        if 'Transpose' in self.ensemble_song.keys():
            for n in self.streamer.recurse().notes:
                n.transpose(self.ensemble_song['Transpose'], inPlace=True)
        
        print(f"Now playing {self.ensemble_song['Title']} ...")
        self.streamer.show("midi")