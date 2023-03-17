class Cell:
    def __init__(self, display_value='.', visible='1', room=-1):
        self.display_value = display_value
        self.visible = visible
        self.room = room

    def get_visible(self):
        return self.visible

    def get_display_value(self):
        return self.display_value

    def get_room(self):
        return self.room

    def set_visible(self, visible):
        self.visible = visible

    def set_room(self, room):
        self.room = room

    def fire_trigger(self, stdscr, testing_board, curr_player, this_game):
        if self.get_display_value() == 'D':
            stdscr.addstr(0, 0, 'D')
            for i in range(len(testing_board.board_list)):
                for j in range(len(testing_board.board_list[i])):
                    if testing_board.board_list[i][j].get_visible() == '1' and (curr_player.get_x() != i or curr_player.get_y() != j):
                        stdscr.addstr(i + testing_board.OFFSET_X, j + testing_board.OFFSET_Y, testing_board.board_list[i][j].get_display_value())

        if self.get_display_value() == 'S':
            stdscr.addstr(0, 0, 'S')
            this_game.move_next_floor(curr_player.get_x(), curr_player.get_y())
            
