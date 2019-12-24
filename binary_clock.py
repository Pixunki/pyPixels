import pixel
import time

if __name__ == '__main__':
    my_playfield = pixel.Field(boards=1, size_board_x=8, size_board_y=5)
    my_cols = my_playfield[0].get_cols()  # we only use the first board

    print(my_cols)
    print([pixel for pixel in my_cols])
    [pixel.paint(pixelexio.COLORS["GREEN"]) for pixelexio in my_cols[0]]
    [pixel.paint(pixelexio.COLORS["RED"]) for pixelexio in my_cols[1]]
    [pixel.paint(pixelexio.COLORS["BLUE"]) for pixelexio in my_cols[2]]
    [pixel.paint(pixelexio.COLORS["WHITE"]) for pixelexio in my_cols[3]]
    [pixel.paint(pixelexio.COLORS["BLACK"]) for pixelexio in my_cols[4]]
    [pixel.paint(pixelexio.COLORS["RED"]) for pixelexio in my_cols[5]]
    [pixel.paint(pixelexio.COLORS["GREEN"]) for pixelexio in my_cols[6]]
    [pixel.paint(pixelexio.COLORS["GREEN"]) for pixelexio in my_cols[7]]

    time.sleep(10)
