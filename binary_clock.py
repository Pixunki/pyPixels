import pixel
import time

if __name__ == '__main__':
    my_playfield = pixel.Field(boards=1, size_board_x=8, size_board_y=5)
    my_cols = my_playfield[0].get_cols()  # we only use the first board

    my_cols[0].paint(pixel.COLORS["GREEN"])
    my_cols[1].paint(pixel.COLORS["RED"])
    my_cols[2].paint(pixel.COLORS["BLUE"])
    my_cols[3].paint(pixel.COLORS["WHITE"])
    my_cols[4].paint(pixel.COLORS["BLACK"])
    my_cols[5].paint(pixel.COLORS["RED"])
    my_cols[6].paint(pixel.COLORS["GREEN"])
    my_cols[7].paint(pixel.COLORS["GREEN"])
