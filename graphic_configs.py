import screeninfo


monitor = screeninfo.get_monitors()[0]
screen_width = monitor.width
screen_height = monitor.height

if screen_width < 1000:
    WIDTH, HEIGHT = 600, 450
    FONT_SIZE = 20
elif screen_width < 2000:
    WIDTH = 800
    HEIGHT = 600
    FONT_SIZE = 25
else:
    WIDTH = (screen_width - screen_width % 400) // 2
    HEIGHT = int(WIDTH * 0.75)
    FONT_SIZE = 30 + (screen_width - 2000) // 75
