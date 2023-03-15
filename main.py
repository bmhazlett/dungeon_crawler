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
        floor_list.append(Floor(vals["board_file"], vals["vis_file"], vals["room_file"]))

    return floor_list
    

def main(stdscr):
    stdscr.clear()
    curses.curs_set(0)

    floor_list = set_up_floors('testing/floors.json')
    this_game = Game(floor_list, floor_list[0], 'floor_mapping')
    
    curr_player = Player('@', 1, 1)
    this_game.curr_floor.update_visiblity(curr_player, stdscr)
    this_game.curr_floor.display_board(curr_player, stdscr)

    while True:
        c = stdscr.getch()

        curr_player.move_player(c, this_game.curr_floor)
        this_game.curr_floor.board_list[curr_player.get_x()][curr_player.get_y()].fire_trigger(stdscr, this_game.curr_floor, curr_player)
        this_game.curr_floor.update_visiblity(curr_player, stdscr)
        this_game.curr_floor.display_board(curr_player, stdscr)

        stdscr.refresh()

wrapper(main)
