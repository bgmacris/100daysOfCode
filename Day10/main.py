import curses
from objetos import Coete

def menu(stdscr):
    height, width = stdscr.getmaxyx()
    k = 0
    cursor_x = width//2
    cursor_y = height-2
    disparo = False

    stdscr.clear()
    stdscr.refresh()

    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Loop where k is the last character pressed
    while (k != ord('q')):

        # Initialization
        stdscr.clear()
        
        if k == curses.KEY_RIGHT:
            cursor_x = cursor_x + 1
        elif k == curses.KEY_LEFT:
            cursor_x = cursor_x - 1
        elif k == ord(' '):
            disparo = True
            coete = Coete((cursor_x, cursor_y-2))
            
            cursor_y = cursor_y - 10

        cursor_x = max(0, cursor_x)
        cursor_x = min(width-1, cursor_x)

        cursor_y = max(0, cursor_y)
        cursor_y = min(height-1, cursor_y)

        # Rendering some text
        whstr = "Width: {}, Height: {}".format(width, height)
        stdscr.addstr(0, 0, whstr, curses.color_pair(1))

        stdscr.move(cursor_y, cursor_x)
        
        if disparo:
            print(coete.get_cordemadas())
            coete_x, coete_y = coete.get_cordemadas()
            print(coete_x, coete_y)
            stdscr.move(coete_x, coete_y)

        # Refresh the screen
        stdscr.refresh()

        # Wait for next input
        k = stdscr.getch()


def main():
    curses.wrapper(menu)


if __name__ == "__main__":
    main()
