from curses import wrapper
import curses
from floor import Floor
from player import Player

OFFSET_X = 1
OFFSET_Y = 1

def main(stdscr):
    stdscr.clear()
    curses.curs_set(0)

    testing_board = Floor('testing/test_board.txt', 'testing/test_vis.txt', 'testing/test_room.txt', 'testing/test_trigger.txt')

    curr_player = Player('@', 1, 1)
    testing_board.display_board(curr_player, stdscr)

    while True:
        c = stdscr.getch()
        stdscr.addstr(curr_player.get_x() + OFFSET_X, curr_player.get_y() + OFFSET_Y, testing_board.board_list[curr_player.get_x()][curr_player.get_y()].get_display_value())

        curr_player.move_player(c, testing_board)
        
        if testing_board.board_list[curr_player.get_x()][curr_player.get_y()].fire_trigger() == "DOOR":
            stdscr.addstr(0, 0, 'h')
            for i in range(len(testing_board.board_list)):
                for j in range(len(testing_board.board_list[i])):
                    if testing_board.board_list[i][j].get_room() == testing_board.board_list[curr_player.get_x()][curr_player.get_y()].get_room():
                        testing_board.board_list[i][j].set_visible('1')

            for i in range(len(testing_board.board_list)):
                for j in range(len(testing_board.board_list[i])):
                    if testing_board.board_list[i][j].get_visible() == '1' and (curr_player.get_x() != i or curr_player.get_y() != j):
                        stdscr.addstr(i + OFFSET_X, j + OFFSET_Y, testing_board.board_list[i][j].get_display_value())

        if testing_board.board_list[curr_player.get_x()][curr_player.get_y()].fire_trigger() == "STAIR":
            pass

        stdscr.addstr(curr_player.get_x() + OFFSET_X, curr_player.get_y() + OFFSET_Y, '@')
        stdscr.refresh()

wrapper(main)

        
    
                
