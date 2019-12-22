import time
import board
import neopixel

COLORS = {
    "BLACK": (0,0,0),
    "WHITE": (255,255,255),
    "BLUE": (255,255,0),
    "RED": (0,255,255),
    "GREEN": (255,0,255)
}
GPIO_PIN = board.D18
COLOR_SETTING = neopixel.GRB

class Field:
    def __init__(self, boards, size_board_x=8, size_board_y=8):
        self.boards = []
        self.neofield = neopixel.NeoPixel(
                            GPIO_PIN,
                            boards*size_board_x*size_board_y,
                            pixel_order=COLOR_SETTING
                        )
        for board_n in range(boards):
            new_board = Board(
                            size_board_x,
                            size_board_y,
                            attached_field = self,
                            start_index = board_n*size_board_x*size_board_y
                        )
            self.boards.append(new_board)
    def __iter__(self, idx):
        yield self.boards[idx]

    def paint(self, color=COLORS["WHITE"]):
        for board in self.boards:
            for row in board:
                for pixel in row:
                    pixel.paint(color)

    def show(self):
        self.neofield.show()

class Board:
    def __init__(self, size_x, size_y, start_index, attached_field):
        self.start_index = start_index
        self.rows = []
        for downwards in range(size_y):
            new_row = Row(
                        size_x,
                        start_index=start_index + size_x*downwards,
                        attached_field = self.attached_field
                    )
            self.rows.append(new_row)

    def __iter__(self, idx):
        yield self.rows[idx]

    def paint(self, color=COLORS["WHITE"]):
        for row in self.rows:
            for row in board:
                for pixel in row:
                    pixel.paint(color)

class Row:
    def __init__(self, size_x, start_index, attached_field):
        self.start_index = start_index
        self.pixels = []
        self.attached_field = attached_field
        for pixel in range(size_x):
            new_pixel = Pixel(
                            index = start_index + pixel,
                            attached_field = self.attached_field
                        )
            self.pixels.append(new_pixel)

    def __iter__(self, idx):
        yield self.pixels[idx]

    def paint(self, color=COLORS["WHITE"]):
        for pixel in self.pixels:
            pixel.paint(color)

class Pixel:
    def __init__(self, idx, attached_field):
        self.index = idx
        self.attached_field = attached_field

    def paint(self, color=COLORS["WHITE"]):
        self.attached_field[self.idx] = color
        self.attached_field.show()


if __name__ == '__main__':
    my_playfield = Field(boards=2, size_board_x=8, size_board_y=8)

    my_playfield.paint((123,231,132))
    time.sleep(0.5)

    my_playfield[0][1][2].paint(COLORS["WHITE"])
    time.sleep(0.5)

    my_playfield[1].paint(COLORS["GREEN"])
    time.sleep(0.5)

    my_playfield[0][3].paint(COLOR["BLUE"])
