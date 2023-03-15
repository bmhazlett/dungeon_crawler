from curses import wrapper
import curses
from floor import Floor
from player import Player
from game import Game

def set_up_floors(mapping_json):
    


def main(stdscr):
    stdscr.clear()
    curses.curs_set(0)

    starting_board = Floor('testing/test_board.txt', 'testing/test_vis.txt', 'testing/test_room.txt')

    this_game = Game('floors', starting_board, 'floor_mapping')
    
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
