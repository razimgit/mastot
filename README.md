# mastot (Modify Audio Speech TO Text)

mastot is a simple command line application built in Python for modifying WAV audiofile and speech recognition (transcription).

Audio modifications include: changing speed (changes duration of the audiofile but doesn't preserve pitch) and changing volume (gain).

Supported languages for speech recognition out-of-the-box are English and Russian. Speech recognition is run by [Vosk](https://alphacephei.com/vosk/).

## Installation

1. Clone this repository
1. Get [poetry](https://python-poetry.org/docs/#installation)
1. Activate a Python 3.11 virtual environment
1. Run following commands:

   ```bash
   poetry install
   make
   ```

   make will download small [models from Vosk](https://alphacephei.com/vosk/models). You can download any model you want if small English and Russian models don't meet your needs.

## Usage

```
> mastot --help

usage: mastot [-h] {modify,transcribe} ... path output

Modify WAV audiofiles or recognize speech in such.

positional arguments:
  {modify,transcribe}  Available functions
    modify             Modify speed and volume
    transcribe         Transcribe English or Russian speech in an audiofile
  path                 Path to a WAV audiofile
  output               Path to a resulting file. A modified audiofile or a transcription in JSON format

options:
  -h, --help           show this help message and exit

> mastot modify --help

usage: mastot modify [-h] [-s [SPEED]] [-v [VOLUME]] [-p]

Modify speed and volume

options:
  -h, --help            show this help message and exit
  -s [SPEED], --speed [SPEED]
                        Speed multiplier like in YouTube. Default: 1. Doesn\'t support "time stretching" (changes duration but doesn\'t preserve pitch)
  -v [VOLUME], --volume [VOLUME]
                        Volume change in decibels. Default: 0
  -p, --percent         If this argument is present, the resulting volume is % of the original volume, similar to VLC's volume slider

> mastot transcribe --help

usage: mastot transcribe [-h] [-l {en,ru}] [-m MODEL]

Transcribe English or Russian speech in an audiofile

options:
  -h, --help            show this help message and exit
  -l {en,ru}, --lang {en,ru}
                        Language of speech in the audiofile. Default: en. Looks for a Vosk model in 'models/lang' directory
  -m MODEL, --model MODEL
                        Path to a directory of a Vosk model. 'lang' parameter is ignored if this is provided
```
