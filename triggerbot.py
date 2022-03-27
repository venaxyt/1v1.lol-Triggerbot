# Made by @venaxyt on Github / forked by @europeans
import pyautogui, win32api, fade, os, threading
from pynput.keyboard import Key, Listener

_key = ""
keybinds = ["1", "2", "3", "f"] # set these to gun keybinds

def getkey(key):
    global _key
    key = str(key).replace("'", "")

    if key not in ["w","a","s","d","Key.space"]: # if it returns movement keys then it wont fire
        _key = key

def listen():
    with Listener(on_press=getkey) as listener:
        listener.join()

def starter_thread():
    thread = threading.Thread(target=listen)
    thread.start()

def main():

    banner = """
     d8b           d8b                        d8,
     88P           88P        d8P            `8P
    d88           d88      d888888P 
    888  ?88   d8P888        ?88'    88bd88b  88b d888b8b   d888b8b   d8888b  88bd88b
    ?88  d88  d8P'?88        88P     88P'  `  88Pd8P' ?88  d8P' ?88  d8b_,dP  88P'  `
     88b ?8b ,88'  88b       88b    d88      d88 88b  ,88b 88b  ,88b 88b     d88
      88b`?888P'    88b      `?8b  d88'     d88' `?88P'`88b`?88P'`88b`?888P'd88'
                  v                     x               )88       )88
                       e     n     a                   ,88P      ,88P
                                                   `?8888P   `?8888P
    """

    print(fade.water(banner))

    screen_resolution = list(map(int,os.popen("wmic path Win32_VideoController get CurrentVerticalResolution,CurrentHorizontalResolution").read().split()[-2::]))  # This line serves to retrieve screen resolution
    screen_length = screen_resolution[0]  # Resolution Length
    screen_height = screen_resolution[1]  # Resolution Height
    actual_x_position = int(screen_length / 2)  # X: Middle of the screen
    actual_y_position = int(screen_height / 2)  # Y: Middle of the screen
    radius = 15  # Recommended ~10/25 (The larger the radius, the larger the circle will be)

    while True:
        # Taking a screenshot of the screen to analyse colors in the defined zone
        screen = pyautogui.screenshot()

        rayon_x = actual_x_position - radius
        rayon_y = actual_y_position - radius

        for x in range(2 * radius):
            if not rayon_x <= 1 and not rayon_y <= 1 and not rayon_x >= 1919 and not rayon_y >= 1079:
                pixel_color = screen.getpixel((rayon_x, rayon_y))

                if pixel_color[0] >= 140 and pixel_color[1] >= 60 and pixel_color[1] <= 135 and pixel_color[2] >= 70 and pixel_color[2] <= 160 and not pixel_color[0] == 204 and not pixel_color[0] == 141:  # Not 141 and 204 colors because 141 is the enemy lifebar of construction and 204 is also the construction's lifebar but of the yours
                    if _key in keybinds: # only firing if the last key pressed was a gun bind, meaning the user has gun selected
                        pyautogui.click()

                rayon_x += 1
                rayon_y += 1

if __name__ == "__main__":
    stater_thread() # starting key checker thread
    main() # starting main process
