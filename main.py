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

def rgb(r, g, b):
    return f"{ESC}[38;2;{r};{g};{b}m"

def bold():
    return f"{ESC}[1m"

def reset():
    return f"{ESC}[0m"

# 🔹 SABİT RENK (burayı değiştirerek ton seçersin)
BASE_COLOR = rgb(0, 200, 255)   # Turkuaz / neon
GLOW_COLOR = rgb(255, 255, 255) # Parlayan harf

def render(name, pos, glow_index):
    spaces = " " * pos
    out = [spaces]

    for i, ch in enumerate(name):
        if i == glow_index:
            out.append(bold() + GLOW_COLOR + ch + reset())
        else:
            out.append(BASE_COLOR + ch + reset())

    return "".join(out)

def animate(name, width=20, delay=0.04, cycles=5):
    hide_cursor()
    try:
        glow = 0

        for _ in range(cycles):
            for pos in range(width + 1):
                clear_line()
                sys.stdout.write(render(name, pos, glow))
                sys.stdout.flush()
                glow = (glow + 1) % len(name)
                time.sleep(delay)

            for pos in range(width, -1, -1):
                clear_line()
                sys.stdout.write(render(name, pos, glow))
                sys.stdout.flush()
                glow = (glow + 1) % len(name)
                time.sleep(delay)

        clear_line()
        print(render(name, 0, -1))
    finally:
        show_cursor()

def main():
    print("✨ Lighty name animation — single color mode")
    name = input("Enter a name (default: Elgiz): ").strip() or "Elgiz"
    animate(name)

if __name__ == "__main__":
    main()
