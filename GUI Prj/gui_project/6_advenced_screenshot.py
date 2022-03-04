import time
import keyboard
from PIL import ImageGrab

def screenshot() :
    # 2022년 3월 4일 7시 26분 20초 -> _20220304_072620
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time))

keyboard.add_hotkey("F9", screenshot)

keyboard.wait("esc")