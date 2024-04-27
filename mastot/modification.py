import math

from pydub import AudioSegment


def modify(path: str, output: str, speed: float, volume: float, in_percent: bool):
    audio = AudioSegment.from_wav(path)
    audio = adjust_speed(audio, speed)
    audio = adjust_volume(audio, volume, in_percent)
    audio.export(output, format="wav")


def adjust_speed(audio: AudioSegment, speed: float):
    if speed <= 0:
        raise ValueError(f"Speed must be positive. Got {speed}")

    # https://stackoverflow.com/a/43438143/9008281
    sound_with_altered_frame_rate = audio._spawn(
        audio.raw_data, overrides={"frame_rate": int(audio.frame_rate * speed)}
    )

    return sound_with_altered_frame_rate.set_frame_rate(audio.frame_rate)


def adjust_volume(audio: AudioSegment, volume: float, in_percent: bool):
    if in_percent:
        if volume < 0:
            raise ValueError(f"Volume in percents must be >= 0. Got {volume}")

        # https://sound.stackexchange.com/a/48502
        db = 25 * math.log(volume / 100) if volume > 0 else -math.inf
    else:
        db = volume

    audio = audio + db

    return audio
