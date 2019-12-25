import pixel as px
from pixel import COLORS as CLR
import time
from datetime import datetime

RED = CLR["RED"]
BLACK = CLR["BLACK"]
BLUE = CLR["BLUE"]

def get_binary_digits(decimal_n, digits=5):
    return format(decimal_n, f"0{digits}b")

def split_two(unit):
    return int(unit[0]), int(unit[1])

def bin_to_led(num, leds, colour=RED, max=0):
    for led in range(len(leds)):
        if num[led]=="1":
            leds[led].paint(RED)
        else:
            leds[led].paint(BLUE)
    for led in range(len(max)):
        leds[led].paint(BLACK)

if __name__ == '__main__':
    my_playfield = px.Field(boards=1, size_board_x=8, size_board_y=5)

    my_cols = my_playfield[0].get_cols()  # we only use the first board
    hr_big, hr_smol = my_cols[0], my_cols[1]
    min_big, min_smol = my_cols[3], my_cols[4]
    sec_big, sec_smol = my_cols[6], my_cols[7]

    while True:
        hour, minute, second = datetime.now().strftime("%H %M %S").split()
        hr, min, sec = split_two(hour), split_two(minute), split_two(second)

        # hour
        bin_to_led(get_binary_digits(hr[0]), hr_big, max=2)
        bin_to_led(get_binary_digits(hr[1]), hr_smol, max=4)

        # minute
        bin_to_led(get_binary_digits(min[0]), min_big, max=3)
        bin_to_led(get_binary_digits(min[1]), min_smol, max=4)

        # second
        bin_to_led(get_binary_digits(sec[0]), sec_big, max=3)
        bin_to_led(get_binary_digits(sec[1]), sec_smol, max=4)

        time.sleep(1)
