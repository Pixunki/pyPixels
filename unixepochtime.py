import pixel as px
import time
from datetime import datetime

RED, BLACK, BLUE = px.COLORS["RED"], px.COLORS["BLACK"], px.COLORS["DARKBLUE"]

def get_binary_digits(decimal_n, digits=5):
    return format(decimal_n, f"0{digits}b")

def split_two(unit):
    return int(unit[0]), int(unit[1])

def bin_to_led(num, leds, colour=RED, max=0):
    for led in range(min(len(leds), 32)):
        print(num)
        if num[led]=="1":
            leds[led].paint(RED)
        else:
            leds[led].paint(BLUE)

if __name__ == '__main__':
    my_playfield = px.Field(boards=1, size_board_x=8, size_board_y=5)
    blob_pixels = my_playfield.get_all()
    print(len(blob_pixels))

    while True:
        now = datetime.now().strftime("%s")
        now_bin = get_binary_digits(int(now), digits=32)
        # hour
        bin_to_led(now_bin, blob_pixels)

        time.sleep(1)
