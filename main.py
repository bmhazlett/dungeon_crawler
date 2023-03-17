import curses
import json
from curses import wrapper
from floor import Floor
from player import Player
from game import Game


def set_up_floors(mapping_json):
    with open(mapping_json) as f:
        data = json.load(f)

    floor_list = []
    for floor in data["Floors"]:
        vals = floor["Floor"]
        floor_list.append(Floor(vals["board_file"], vals["vis_file"], vals["room_file"], vals["floor_name"]))

    return floor_list


def set_up_mapping(stair_mapping_json):
    with open(stair_mapping_json) as f:
        data = json.load(f)
    
    return data


def main(stdscr):
    ofp = open('output', 'w')
    stdscr.clear()
    curses.curs_set(0)

    floor_list = set_up_floors('testing/floors.json')
    stair_mapping = set_up_mapping('testing/stair_mapping.json')
    this_game = Game(floor_list, floor_list[0], stair_mapping)

    curr_player = Player('@', 1, 1)
    this_game.curr_floor.update_visiblity(curr_player, stdscr)
    this_game.curr_floor.display_board(curr_player, stdscr)

    for floor in this_game.floors:
        for i in range(len(floor.board_list)):
            for j in range(len(floor.board_list[i])):
                ofp.write(floor.board_list[i][j].get_visible())
            ofp.write('\n')
        ofp.write('\n')

    while True:
        #### Debug ####
        stdscr.addstr(0, 3, str(curr_player.get_x()))
        stdscr.addstr(0, 6, str(curr_player.get_y()))        
        stdscr.addstr(0, 9, this_game.curr_floor.get_floor_name())
        #### Debug ####
        
        c = stdscr.getch()

        curr_player.move_player(c, this_game.curr_floor)
        this_game.curr_floor.board_list[curr_player.get_x()][curr_player.get_y()].fire_trigger(stdscr, this_game.curr_floor, curr_player, this_game)
        this_game.curr_floor.update_visiblity(curr_player, stdscr)
        this_game.curr_floor.display_board(curr_player, stdscr)

        stdscr.refresh()

wrapper(main)
