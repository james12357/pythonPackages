import socket
from PIL import Image
import pyautogui
import io
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
p = 12366
s.connect((host, p))
while True:
    # time.sleep(5)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, p))
    a = pyautogui.screenshot()
    bt = io.BytesIO()
    a.save(bt, format="JPEG")
    s.send(bt.getvalue())
    s.close()

