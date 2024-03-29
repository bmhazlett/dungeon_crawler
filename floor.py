from cell import Cell

class Floor:
    def __init__(self, map_path: str, starting_visiblity_mapping_path: str, room_path: str, floor_name: str):
        self.board_list = self.read_in_map(map_path, starting_visiblity_mapping_path, room_path)
        self.floor_name = floor_name
        self.OFFSET_X = 1
        self.OFFSET_Y = 1

    def get_floor_name(self):
        return self.floor_name

    def set_floor_name(self, floor_name):
        self.floor_name = floor_name

    def read_in_map(self, map_path: str, starting_visibility_mapping_path: str, room_path: str):
        mfp = open(map_path)
        vfp = open(starting_visibility_mapping_path)
        rfp = open(room_path)

        map_string = mfp.read().splitlines()
        vis_string = vfp.read().splitlines()
        room_string = rfp.read().splitlines()

        x_length = len(map_string)
        y_length = len(map_string[0])
        temp_board = []

        for i in range(len(map_string)):
            temp_board.append([])
            for j in range(len(map_string[i])):
                new_cell = Cell(map_string[i][j], vis_string[i][j], room_string[i][j])
                temp_board[i].append(new_cell)

        return temp_board

    def display_board(self, curr_player, stdscr):
        for i in range(len(self.board_list)):
            for j in range(len(self.board_list[i])):
                if self.board_list[i][j].get_visible() == '1' and (curr_player.get_x() != i or curr_player.get_y() != j):
                    stdscr.addstr(i + self.OFFSET_X, j + self.OFFSET_Y, self.board_list[i][j].get_display_value())

                if self.board_list[i][j].get_visible() == '1' and (curr_player.get_x() == i and curr_player.get_y() == j):
                    stdscr.addstr(i + self.OFFSET_X, j + self.OFFSET_Y, curr_player.get_display_value())

                if self.board_list[i][j].get_visible() == '0':
                    stdscr.addstr(i + self.OFFSET_X, j + self.OFFSET_Y, ' ')
                    

    def update_visiblity(self, curr_player, stdscr):
        output_file = open('output', 'a')
        for i in range(len(self.board_list)):
            for j in range(len(self.board_list[i])):
                output_file.write(str(len(self.board_list)) + ' '  + str(len(self.board_list[i])) + '\n')
                if self.board_list[i][j].get_room() == self.board_list[curr_player.get_x()][curr_player.get_y()].get_room():
                    self.board_list[i][j].set_visible('1')
