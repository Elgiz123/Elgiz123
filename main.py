import sys
import time

ESC = "\x1b"

def hide_cursor():
    sys.stdout.write(f"{ESC}[?25l")
    sys.stdout.flush()

def show_cursor():
    sys.stdout.write(f"{ESC}[?25h")
    sys.stdout.flush()

def clear_line():
    sys.stdout.write(f"\r{ESC}[2K")
    sys.stdout.flush()

def rgb(r: int, g: int, b: int) -> str:
    # Truecolor (24-bit) foreground
    return f"{ESC}[38;2;{r};{g};{b}m"

def bold(on: bool = True) -> str:
    return f"{ESC}[1m" if on else f"{ESC}[22m"

def reset() -> str:
    return f"{ESC}[0m"

def lerp(a: int, b: int, t: float) -> int:
    return int(a + (b - a) * t)

def gradient_color(i: int, n: int) -> str:
    # Mor -> Mavi -> Turkuaz gradient
    if n <= 1:
        t = 0.0
    else:
        t = i / (n - 1)

    # iki aşamalı gradient: (160,80,255) -> (70,120,255) -> (0,220,200)
    if t < 0.5:
        t2 = t / 0.5
        r = lerp(160, 70, t2)
        g = lerp(80, 120, t2)
        b = lerp(255, 255, t2)
    else:
        t2 = (t - 0.5) / 0.5
        r = lerp(70, 0, t2)
        g = lerp(120, 220, t2)
        b = lerp(255, 200, t2)

    return rgb(r, g, b)

def render(name: str, pos: int, glow_index: int) -> str:
    # pos: soldan boşluk
    spaces = " " * max(0, pos)
    out = [spaces]

    for i, ch in enumerate(name):
        color = gradient_color(i, len(name))
        # glow: bir harfi daha parlak/bold yap
        if i == glow_index:
            out.append(bold(True) + rgb(255, 255, 255) + ch + reset())
        else:
            out.append(color + ch + reset())

    return "".join(out)

def animate(name: str, width: int = 24, delay: float = 0.04, cycles: int = 4):
    hide_cursor()
    try:
        glow = 0
        d
