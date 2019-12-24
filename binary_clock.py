import pixel
import time

if __name__ == '__main__':
    my_playfield = pixel.Field(boards=1, size_board_x=8, size_board_y=5)
    my_cols = my_playfield[0].get_cols()  # we only use the first board

    print(my_cols)
    print([pixel for pixel in my_cols])
    [pixelexio.paint(pixel.COLORS["GREEN"]) for pixelexio in my_cols[0]]
    [pixelexio.paint(pixel.COLORS["RED"]) for pixelexio in my_cols[1]]
    [pixelexio.paint(pixel.COLORS["BLUE"]) for pixelexio in my_cols[2]]
    [pixelexio.paint(pixel.COLORS["WHITE"]) for pixelexio in my_cols[3]]
    [pixelexio.paint(pixel.COLORS["BLACK"]) for pixelexio in my_cols[4]]
    [pixelexio.paint(pixel.COLORS["RED"]) for pixelexio in my_cols[5]]
    [pixelexio.paint(pixel.COLORS["GREEN"]) for pixelexio in my_cols[6]]
    [pixelexio.paint(pixel.COLORS["GREEN"]) for pixelexio in my_cols[7]]

    time.sleep(10)
