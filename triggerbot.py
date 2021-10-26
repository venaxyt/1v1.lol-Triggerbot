# Made by @venaxyt on Github
import pyautogui, win32api, fade, os

os.system("cls")

# Editing this banner will not make you a developer
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

#supporter resolution
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

            if pixel_color[0] >= 140 and pixel_color[1] >= 60 and pixel_color[1] <= 135 and pixel_color[2] >= 70 and pixel_color[2] <= 160:
                pyautogui.click()

            rayon_x += 1
            rayon_y += 1
