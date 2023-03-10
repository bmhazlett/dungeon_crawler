from cell import Cell

class Floor:
    def __init__(self, map_path: str, starting_visiblity_mapping_path: str, room_path: str, trigger_path: str):
        self.board_list = self.read_in_map(map_path, starting_visiblity_mapping_path, room_path, trigger_path)

    def read_in_map(self, map_path: str, starting_visibility_mapping_path: str, room_path: str, trigger_path: str):
        mfp = open(map_path)
        vfp = open(starting_visibility_mapping_path)
        rfp = open(room_path)
        tfp = open(trigger_path)

        map_string = mfp.read().splitlines()
        vis_string = vfp.read().splitlines()
        room_string = rfp.read().splitlines()
        trigger_string = tfp.read().splitlines()

        x_length = len(map_string)
        y_length = len(map_string[0])
        temp_board = []

        ofp = open('output', 'w')
        for i in range(len(map_string)):
            temp_board.append([])
            for j in range(len(map_string[i])):
                ofp.write(str(len(map_string)) + " " +  str(len(vis_string)) + " " +  str(len(room_string)) + " " +  str(len(trigger_string)))
                ofp.write(str(len(map_string[i])) + " " +  str(len(vis_string[i])) + " " +  str(len(room_string[i])) + " " +  str(len(trigger_string[i])))
                new_cell = Cell(map_string[i][j], vis_string[i][j], room_string[i][j], trigger_string[i][j])
                temp_board[i].append(new_cell)

        return temp_board