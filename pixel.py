import time
import board
import neopixel

COLORS = {
    "BLACK": (0,0,0),
    "WHITE": (255,255,255),
    "BLUE": (0,0,255),
    "RED": (255,0,0),
    "GREEN": (0,255,0)
}
GPIO_PIN = board.D12
COLOR_SETTING = neopixel.GRB

class Field:
    def __init__(self, boards, size_board_x=8, size_board_y=8, \
                pin=GPIO_PIN, setting=COLOR_SETTING):
        self.boards = []
        self.neofield = neopixel.NeoPixel(
                            GPIO_PIN,
                            boards*size_board_x*size_board_y,
                            pixel_order = COLOR_SETTING,
                            brightness = 0.04
                        )

        for board_n in range(boards):
            new_board = Board(
                            size_board_x,
                            size_board_y,
                            attached_field = self,
                            start_index = board_n*size_board_x*size_board_y
                        )
            self.boards.append(new_board)
    def __iter__(self):
        for board in self.boards:
            yield board

    def paint(self, color=COLORS["WHITE"]):
        for board in self.boards:
            for row in board:
                for pixel in row:
                    pixel.paint(color)

    def __setitem__(self, idx, val):
        self.neofield[idx] = val
    def __getitem__(self, idx):
        return self.boards[idx]

    def show(self):
        self.neofield.show()

    def get_cols(self):
        return [board.get_cols() for board in self]

    def __len__(self):
        return len(self.boards)

class Board:
    def __init__(self, size_x, size_y, start_index, attached_field):
        self.start_index = start_index
        self.attached_field = attached_field
        self.rows = []
        for downwards in range(size_y):
            new_row = Row(
                        size_x,
                        start_index=start_index + size_x*downwards,
                        attached_field = self.attached_field
                    )
            self.rows.append(new_row)

    def __iter__(self):
        for row in self.rows:
            yield row

    def paint(self, color=COLORS["WHITE"]):
        for row in self.rows:
            for pixel in row:
                pixel.paint(color)
    def show(self):
        self.attached_field.show()

    def __getitem__(self, idx):
        return self.rows[idx]

    def get_cols(self):
        columns = []
        n_cols = len(self[0])

        for column in range(n_cols):
            new_col = []
            for row in self:
                new_col.append(row[column])
            columns.append(new_col)
            new_col.clear()
        return columns

    def __len__(self):
        return len(self.rows)


class Row:
    def __init__(self, size_x, start_index, attached_field):
        self.start_index = start_index
        self.pixels = []
        self.attached_field = attached_field
        for pixel in range(size_x):
            new_pixel = Pixel(
                            idx = start_index + pixel,
                            attached_field = self.attached_field
                        )
            self.pixels.append(new_pixel)

    def __iter__(self):
        for pixel in self.pixels:
            yield pixel

    def paint(self, color=COLORS["WHITE"]):
        for pixel in self.pixels:
            pixel.paint(color)
    def show(self):
        self.attached_field.show()


    def __getitem__(self, idx):
        return self.pixels[idx]

    def __len__(self):
        return len(self.pixels)

class Pixel:
    def __init__(self, idx, attached_field):
        self.index = idx
        self.attached_field = attached_field

    def paint(self, color=COLORS["WHITE"]):
        self.attached_field[self.index] = color

    def show(self):
        self.attached_field.show()


if __name__ == '__main__':
    my_playfield = Field(boards=2, size_board_x=8, size_board_y=8)

    # my_playfield.paint((123,231,132))
    # time.sleep(0.5)
    #
    # my_playfield[0][1][2].paint(COLORS["WHITE"])
    # my_playfield.show()
    # time.sleep(0.5)
    #
    # my_playfield[1].paint(COLORS["GREEN"])
    # my_playfield.show()
    # time.sleep(0.5)
    #
    # my_playfield[0][3].paint(COLORS["BLUE"])
    # my_playfield.show()

    for row in range(8):
        for board in my_playfield:
            for pixel in board[row]:
                pixel.paint(COLORS["GREEN"])
                pixel.show()
                time.sleep(0.3)
