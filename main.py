#!/usr/bin/python3
import pygame as pg  # type: ignore
from pygame.time import Clock  # type: ignore

from events import events_map

from config import CHANNELS


def init() -> Clock:
    print(events_map)

    pg.init()
    pg.display.set_mode((800, 800), pg.RESIZABLE)

    pg.mixer.init()
    pg.mixer.set_num_channels(CHANNELS)

    # Init joystick. Currently only one.
    try:
        pg.joystick.init()
        for j in range(pg.joystick.get_count()):
            pg.joystick.Joystick(j).init()
    except pg.error:
        print("Joystick error")
        quit()

    return Clock()


def loop(clock: Clock):
    while True:
        event = pg.event.poll()
        if not event.type:
            clock.tick(60)
        elif event.type in events_map:
            print(f"Type: {event.type}")
            events_map[event.type].exec(event)
            pg.event.clear()
        else:
            print(f"Ignored: {event.type}")


def main():
    clock = init()
    loop(clock)


if __name__ == "__main__":
    main()
