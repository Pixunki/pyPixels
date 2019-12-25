import pixel as px
from pixel import COLORS as CLR
import time
from datetime import datetime

RED = CLR["RED"]

if __name__ == '__main__':
    my_playfield = px.Field(boards=1, size_board_x=8, size_board_y=5)

    my_cols = my_playfield[0].get_cols()  # we only use the first board
    hr_big, hr_smol = my_cols[0], my_cols[1]
    min_big, min_smol = my_cols[3], my_cols[4]
    sec_big, sec_smol = my_cols[6], my_cols[7]

    px.Row.paint(hr_big, RED)
    px.Row.paint(hr_smol, RED)
    px.Row.paint(min_big, RED)
    px.Row.paint(min_smol, RED)
    px.Row.paint(sec_big, RED)
    px.Row.paint(sec_smol, RED)

    while True:
        hour, minute, second = datetime.now().strftime("%H %M %S").split()
        print(hour, minute, second)
        hour_big, hour_smol = int(hour[0]), int(hour[1])
        minute_big, minute_smol = int(minute[0]), int(minute[1])
        second_big, second_smol = int(second[0]), int(second[1])

        for unit in [hour_big, hour_smol,
                    minute_big, minute_smol,
                    second_big, second_smol]:
            print(format(unit, "05b"))

        time.sleep(1)
