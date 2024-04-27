import json
import logging

from pydub import AudioSegment
from vosk import KaldiRecognizer, Model, SetLogLevel

logger = logging.getLogger(__name__)
FRAME_RATE = 16000

SetLogLevel(-1)


def transcribe(path: str, output: str, model: str):
    audio = AudioSegment.from_wav(path)
    # "When using your own audio file make sure it has the correct format
    # - PCM 16khz 16bit mono" https://alphacephei.com/vosk/install
    audio = audio.set_frame_rate(FRAME_RATE)
    audio = audio.set_channels(1)

    logger.info("Initializing model...")
    model = Model(model_path=model)

    rec = KaldiRecognizer(model, FRAME_RATE)
    rec.SetWords(True)
    rec.SetPartialWords(True)

    # Преобразуем вывод в json
    logger.info("Transcribing...")
    rec.AcceptWaveform(audio.raw_data)
    result = rec.FinalResult()

    print("Recognized text:")
    print(json.loads(result)["text"])

    with open(output, "w", encoding="UTF-8") as f:
        f.write(result)
