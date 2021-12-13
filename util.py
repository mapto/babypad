from os.path import isfile

from pygame import mixer  # type: ignore

from config import CHANNELS, FORMAT


def playsound(snd: str):
    fname = f"sounds/{snd}.{FORMAT}"
    if isfile(fname):
        ch = mixer.find_channel(True)
        snd = mixer.Sound(file=fname)
        ch.set_volume(mixer.music.get_volume())
        ch.play(snd)
    else:
        print(f"Not found: {fname}")


def bound(v):
    if v > 1:
        return 1
    elif v < 0:
        return 0
    else:
        return v
