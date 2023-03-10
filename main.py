from curses import wrapper
import curses
from floor import Floor

OFFSET_X = 1
OFFSET_Y = 1

def main(stdscr):
    stdscr.clear()
    curses.curs_set(0)

    testing_board = Floor('testing/test_board.txt', 'testing/test_vis.txt', 'testing/test_room.txt', 'testing/test_trigger.txt')

    curr_pos = [1, 1]
    for i in range(len(testing_board.board_list)):
        for j in range(len(testing_board.board_list[i])):
            if testing_board.board_list[i][j].get_room() == testing_board.board_list[curr_pos[0]][curr_pos[1]].get_room():
                stdscr.addstr(i + OFFSET_X, j + OFFSET_Y, testing_board.board_list[i][j].get_display_value())
            if i == curr_pos[0] and j == curr_pos[1]:
                stdscr.addstr(i + OFFSET_X, j + OFFSET_Y, '@')

    stdscr.refresh()

    while True:
        c = stdscr.getch()
        stdscr.addstr(curr_pos[0] + OFFSET_X, curr_pos[1] + OFFSET_Y, testing_board.board_list[curr_pos[0]][curr_pos[1]].get_display_value())
        if c == ord('a'):
            if testing_board.board_list[curr_pos[0]][curr_pos[1] - 1].get_display_value() != '#':
                curr_pos[1] -= 1
        elif c == ord('d'):
            if testing_board.board_list[curr_pos[0]][curr_pos[1] + 1].get_display_value() != '#':
                curr_pos[1] += 1
        elif c == ord('w'):
            if testing_board.board_list[curr_pos[0] - 1][curr_pos[1]].get_display_value() != '#':
                curr_pos[0] -= 1
        elif c == ord('s'):
            if testing_board.board_list[curr_pos[0] + 1][curr_pos[1]].get_display_value() != '#':
                curr_pos[0] += 1

        if testing_board.board_list[curr_pos[0]][curr_pos[1]].fire_trigger() == "DOOR":
            stdscr.addstr(0, 0, 'h')
            for i in range(len(testing_board.board_list)):
                for j in range(len(testing_board.board_list[i])):
                    if testing_board.board_list[i][j].get_room() == testing_board.board_list[curr_pos[0]][curr_pos[1]].get_room():
                        testing_board.board_list[i][j].set_visible('1')

            for i in range(len(testing_board.board_list)):
                for j in range(len(testing_board.board_list[i])):
                    if testing_board.board_list[i][j].get_visible() == '1' and (curr_pos[0] != i or curr_pos[1] != j):
                        stdscr.addstr(i + OFFSET_X, j + OFFSET_Y, testing_board.board_list[i][j].get_display_value())

        if testing_board.board_list[curr_pos[0]][curr_pos[1]].fire_trigger() == "STAIR":
            pass

        stdscr.addstr(curr_pos[0] + OFFSET_X, curr_pos[1] + OFFSET_Y, '@')
        stdscr.refresh()

wrapper(main)

        
    
                
