class Player:
    def __init__(self, display_value, x, y):
        self.display_value = display_value
        self.x = x
        self.y = y

    def get_display_value(self):
        return self.display_value

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_display_value(self, display_value):
        self.display_value = display_value

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def move_player(self, c, curr_board):
        if c == ord('a'):
            if curr_board.board_list[self.x][self.y - 1].get_display_value() != '#':
                self.y -= 1
        elif c == ord('d'):
            if curr_board.board_list[self.x][self.y + 1].get_display_value() != '#':
                self.y += 1
        elif c == ord('w'):
            if curr_board.board_list[self.x - 1][self.y].get_display_value() != '#':
                self.x -= 1
        elif c == ord('s'):
            if curr_board.board_list[self.x + 1][self.y].get_display_value() != '#':
                self.x += 1

