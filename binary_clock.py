import pixel
import time

if __name__ == '__main__':
    my_playfield = pixel.Field(boards=1, size_board_x=8, size_board_y=5)
    my_cols = my_playfield[0].get_cols()  # we only use the first board

    [pixel.paint(pixel.COLORS["GREEN"]) for pixel in my_cols[0]]
    [pixel.paint(pixel.COLORS["RED"]) for pixel in my_cols[1]] 
    [pixel.paint(pixel.COLORS["BLUE"]) for pixel in my_cols[2]]
    [pixel.paint(pixel.COLORS["WHITE"]) for pixel in my_cols[3]]
    [pixel.paint(pixel.COLORS["BLACK"]) for pixel in my_cols[4]]
    [pixel.paint(pixel.COLORS["RED"]) for pixel in my_cols[5]]
    [pixel.paint(pixel.COLORS["GREEN"]) for pixel in my_cols[6]]
    [pixel.paint(pixel.COLORS["GREEN"]) for pixel in my_cols[7]]

    time.sleep(10)
