import pixel as px
from pixel import COLORS as CLR
import time

RED = CLR["RED"]

if __name__ == '__main__':
    my_playfield = px.Field(boards=1, size_board_x=8, size_board_y=5)
    my_cols = my_playfield[0].get_cols()  # we only use the first board

    print(my_cols)
    print([pixel for pixel in my_cols])
    hr_big = my_cols[0]
    hr_smol = my_cols[1]

    min_big = my_cols[3]
    min_smol = my_cols[4]

    sec_big = my_cols[6]
    sec_smol = my_cols[7]

    px.Row.paint(hr_big, RED)
    px.Row.paint(hr_smol, RED)
    px.Row.paint(min_big, RED)
    px.Row.paint(min_smol, RED)
    px.Row.paint(sec_big, RED)
    px.Row.paint(sec_smol, RED)


    time.sleep(10)
