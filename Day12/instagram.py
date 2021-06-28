import wget
import os
import requests
import curses

global headers, url
headers = {
    'x-rapidapi-key': 'TOKEN',
    'x-rapidapi-host': 'HOST'
}
url = 'https://instagram-data1.p.rapidapi.com/'


# os.system('cls')

# print("Selecciona la opcion que necesitas")
# payload = requests.get(url, headers=headers, params=params)
# print(payload.text)


def my_raw_input(stdscr, r, c, prompt_string):
    curses.echo()
    stdscr.addstr(r, c, prompt_string)
    stdscr.refresh()
    input = stdscr.getstr(r + 1, c, 20)
    return input  #



def menu(stdscr):
    height, width = stdscr.getmaxyx()
    k = 0
    cursor_x = width//2
    cursor_y = height-2

    stdscr.clear()
    stdscr.refresh()

    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)


    # Loop where k is the last character pressed
    while (k != ord('q')):
        stdscr.clear()
        # stdscr.addch(width, height, curses.ACS_PI)
        whstr = "Seleccione una de las siguientes opciones pulsando \nel numero correpondiente a cada una:"
        stdscr.addstr(0, 0, whstr, curses.color_pair(1))
        opt1 = "1 -> Descargar foto de perfil de un usuario"
        stdscr.addstr(3, 0, opt1, curses.color_pair(3))
        opt2 = "2 -> Optener videos de las Stories"
        stdscr.addstr(4, 0, opt2, curses.color_pair(3))
        if k == ord('1'):
            name_user = my_raw_input(stdscr, 20, 50, "Introduce el nombre de usuario")
            params = {"keyword": name_user.decode('utf-8')}
            payload = requests.get(url+'user/search', headers=headers, params=params).json()
            img_url = payload[0]['user']['profile_pic_url']
            print(img_url)
            local_image_filename = wget.download(img_url)

        if k == ord("2"):
            name_user = my_raw_input(stdscr, 20, 50, "Introduce el nombre de usuario")
            params = {"username": name_user.decode('utf-8')}
            payload = requests.get(url+'/location/fee1d', headers=headers, params=params)
            print(payload.text)

        stdscr.move(cursor_y, cursor_x)

        # Refresh the screen
        stdscr.refresh()

        # Wait for next input
        k = stdscr.getch()


def main():
    curses.wrapper(menu)


if __name__ == "__main__":
    main()
