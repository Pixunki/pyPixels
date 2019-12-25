import pixel as px
from pixel import COLORS as CLR
import time

if __name__ == '__main__':
    my_playfield = px.Field(boards=1, size_board_x=8, size_board_y=5)
    my_cols = my_playfield[0].get_cols()  # we only use the first board

    print(my_cols)
    print([pixel for pixel in my_cols])
    px.Row.paint(my_cols[0], CLR["GREEN"])
    px.Row.paint(my_cols[1], CLR["BLUE"])
    px.Row.paint(my_cols[2], CLR["BLACK"])
    px.Row.paint(my_cols[3], CLR["RED"])
    px.Row.paint(my_cols[4], CLR["WHITE"])
    px.Row.paint(my_cols[5], CLR["BLACK"])
    px.Row.paint(my_cols[6], CLR["GREEN"])
    px.Row.paint(my_cols[7], CLR["RED"])


    time.sleep(10)
