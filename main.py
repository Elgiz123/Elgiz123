import sys
import time

ESC = "\x1b"

def hide_cursor():
    sys.stdout.write(f"{ESC}[?25l")
    sys.stdout.flush()

def show_cursor():
    sys.stdout.write(f"{ESC}[?25h")
    sys.stdout.flush()

def clear_screen():
    sys.stdout.write(f"{ESC}[2J{ESC}[H")  # clear + home
    sys.stdout.flush()

def rgb(r, g, b):
    return f"{ESC}[38;2;{r};{g};{b}m"

def reset():
    return f"{ESC}[0m"

def bold(on=True):
    return f"{ESC}[1m" if on else f"{ESC}[22m"

def center(text: str, width: int) -> str:
    if len(text) >= width:
        return text
    left = (width - len(text)) // 2
    return " " * left + text

def heartbeat(name: str, width: int = 60, beats: int = 30, bpm: int = 90):
    # Tek renk tonu (istersen değiştir)
    BASE = rgb(0, 200, 255)     # neon turkuaz
    DIM  = rgb(0, 120, 160)     # sönük ton
    NAME = bold(True) + rgb(255, 255, 255)  # isim beyaz-kalın

    # Nabız karakterleri (daha "soft" istersen: "·", "•", "○", "◌")
    ring_chars = ["·", "•", "●", "█", "●", "•", "·"]

    # BPM -> saniye per beat (yaklaşık)
    beat_period = 60.0 / max(30, bpm)  # aşırı hızlı olmasın
    frame_delay = beat_period / 7.0

    hide_cursor()
    try:
        for _ in range(beats):
            for k, ch in enumerate(ring_chars):
                clear_screen()

                # Nabız halkası: üst/alt çizgi + yanlarda “ch”
                line = ch * max(0, min(width, len(name) + 18))
                top = DIM + center(line, width) + reset()
                mid_left = DIM + ch * 3 + reset()
                mid_right = DIM + ch * 3 + reset()

                name_line = (
                    " " * ((width - len(name)) // 2 - 3)
                    + mid_left
                    + reset()
                    + BASE + " "  # ufak
