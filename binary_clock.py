import pixel as px
import time
from datetime import datetime

RED, BLACK, BLUE, GREEN = px.COLORS["RED"], px.COLORS["BLACK"], px.COLORS["DARKBLUE"], px.COLORS["DARKGREEN"]
LENGTH_Y = 8


def get_binary_digits(decimal_n, digits=LENGTH_Y):
    return format(decimal_n, f"0{digits}b")

def split_two(unit):
    return int(unit[0]), int(unit[1])

def bin_to_led(num, leds, colour=RED, max=0):
    for led in range(len(leds)):
        if len(leds)-max > led:
            leds[led].paint(BLACK)
        elif num[led]=="1":
            leds[led].paint(RED)
        else:
            leds[led].paint(BLUE)

def init():
    my_playfield = px.Field(boards=1, size_board_x=8, size_board_y=LENGTH_Y)
    return my_playfield

def main(my_playfield):
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
    return my_playfield

if __name__ == "__main__":
    my_pf = init()
    try:
        main(my_pf)
    except KeyboardInterrupt:
        my_pf.paint(BLACK)
