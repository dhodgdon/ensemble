# Ensemble

**Ensemble** is a domain-specific programming language for creating musical programs in a way intuitive to those familiar with sheet music. 

Ensemble uses [scientific pitch notation](https://www.musicandtheory.com/an-easy-guide-to-scientific-pitch-notation/) and other grammatical elements recognizable by musicians. It is meant to be used by those with little to no programming experience as well as experienced programmers.

Please follow the link below to get started:

[Ensemble Download Instructions](download_instructions.md#ensemble-installation-instructions)

## Examples

Ensemble files have the following characteristics (Note: This order must be followed.): 
* Title
* Tempo
* Time Signature
* Transpose (optional)
* At least one line of music
* Comments, which are specified by `#` (everything that comes after `#` to the end of the line is ignored)

Here is an example of a basic Ensemble file that plays C4 four times:

    Title: "My Basic Ensemble File"
    Tempo: 100
    Time Signature: 4/4
    Transpose: +12  # THIS LINE IS OPTIONAL

        [C4, C4, C4, C4]

### Title

Title can be made up of any characters enclosed in double quotation marks. (The only exception to this are double quotation marks themselves, which are not allowed in the Title. If you need to use quotation marks in the Title, use single quotation marks.)

### Tempo

Tempo always refers to quarter notes beats per minute (BPM).

### Time Signature

Time Signature is very flexible and can be chosen from many common (and uncommon) time signatures, including 4/4 (common time), 3/4 (waltz time), 2/4 (cut time), 6/8 (compound duple), 9/8 (compound triple), 12/8 (compound quadruple), 5/4, 7/8, 3/8, 2/2 (alla breve), 4/2, 5/8, 7/4, 11/8, 6/4, 9/4, 13/8, 15/8, 10/8, 3/2, 2/8, 4/16, 3/16, 5/16, 6/16, 7/16, 9/16, 12/16, 9/32, 12/32, 5/2, 7/2, 13/4, 21/8, and 17/16.

### Transpose

Transpose is an optional line that allows you to specify how many half steps to transpose the notes in your Ensemble file. You must have either `+` or `-` before the number on this line so that Ensemble knows whether to transpose to a higher pitch or lower pitch respectively.

### Lines of Music/Parts

Every Ensemble file consists of one or more lines of music, each of which is a separate part or voice. A line of music begins with `[` and ends with `]`. Between these square brackets, there are [notes](#notes), separated by [measures](#measures). The total quantity of notes/beats in each measure must follow your Time Signature. For example, if you specify your Time Signature as 4/4 then you must have enough notes in the measure that their length combined is that of four quarter notes. (Note: Ensemble will throw an error if there is an incorrect number of notes/beats in one of your measures.)

Note the distinction that each line of music in Ensemble is a part and not the same as a line of sheet music. In sheet music, you may have 10 lines of music in a song, each line containing multiple parts. In Ensemble, you have one line per part in a song so that each line extends to the end of the song.

For example, in the following sheet music there are four vocal parts - soprano, alto, tenor, and bass - each of which would be one line in an Ensemble file. (If you wanted the accompaniment, you would need to add more lines/parts accordingly.)

![Handel's Messiah](images/handel_messiah.png)
*Sheet music from [free-scores.com](https://www.free-scores.com/)*

The four vocal parts can be represented as follows in Ensemble:

    Title: "No. 12 - CHORUS, 'For Unto Us a Child Is Born'"
    Tempo: 76
    Time Signature: 4/4

        # Soprano part
        [<<the entire soprano part goes here>>]
        
        # Alto part
        [<<the entire alto part goes here>>]

        # Tenor part
        [<<the entire tenor part goes here>>]

        # Bass part
        [<<the entire bass part goes here>>]

I intentionally left out the implementation of the notes in each part to focus on the conversion from sheet music into an Ensemble program. Now that we understand implementation for lines of music/parts in an Ensemble program, we are ready to tackle implementing notes.

### Notes

#### Note

Notes in Ensemble follow [scientific pitch notation](https://www.musicandtheory.com/an-easy-guide-to-scientific-pitch-notation/).



#### Rest

Rests in Ensemble are shown by two dashes `--`.

#### Hold

Holds in Ensemble are shown by two tildes `~~`.

### Measures

Measures in Ensemble are shown by a single bar `|`.

## Installation

## Bug Reports

## Contributing

## License

Ensemble is licensed under the [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0).