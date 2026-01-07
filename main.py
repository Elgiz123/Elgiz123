import sys
import time


def build_lighty_frame(name, active_index):
    dim = "\033[2m"
    bright = "\033[1m"
    reset = "\033[0m"
    chars = []
    for index, char in enumerate(name):
        if index == active_index:
            chars.append(f"{bright}{char}{reset}")
        else:
            chars.append(f"{dim}{char}{reset}")
    return " ".join(chars)


def animate_name(name, cycles=3, delay=0.12):
    if not name:
        return
    length = len(name)
    for _ in range(cycles):
        for index in range(length):
            frame = build_lighty_frame(name, index)
            sys.stdout.write(f"\r{frame}")
            sys.stdout.flush()
            time.sleep(delay)
    sys.stdout.write("\n")


def main():
    print("Lighty name animation")
    user_name = input("Enter a name (default: Elgiz): ").strip() or "Elgiz"
    animate_name(user_name)

if __name__ == "__main__":
    main()
