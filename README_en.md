# Text to Speech in Serbian Language 🇷🇸
**ANDREJ RAJKOV - PETNICA PROJECT 2021**

The first version of TTS in Serbian.

This program converts the desired text from a text file to speech as an audio file.

## How it works

+ The project is / will be done in Python completely.
+ The project uses the [PYDUB](http://pydub.com/) library to manipulate sound.
+ In its most basic form (version 1.0), the program takes letters and pauses from a string and appends audio files with that letter's name.
```
for x in string:
    combined + = AudioSegment.from_mp3 (x + ". mp3")
```
## NOTE

+ This version of TTS is **not** the final version, but only a proof of concept.
+ In the final version, v2.0, better audio libraries, accentation, punctuation will be implemented.
There is a possibility of introducing context algorithms in future versions.

## Requirements

The program has been tested on Linux, but probably works on Windows as well.

+ [FFMPEG](https://ffmpeg.org/)

## Further developement

The following improvements are planned for the next version:

+ New audio library (engine will have a smoother and more natural pronunciation of letters and words)
+ Accentation according to the rules of the Serbian language (word modulation - length and tone change)
+ Punctuation (change of tone depending on .,!?)
+ Add a simple GUI and add an EXE file

Later versions will also include:

+ Algorithms for context (solves problems like Luka/ luka, da dâ)
