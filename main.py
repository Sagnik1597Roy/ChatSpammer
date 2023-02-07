import time
import pyautogui #pip install pyautogui
import random
import pyperclip #pip install pyperclip

a = ["Hello", "Hi", "Are you Lost!!", "LOL", "How are you", "What", "Nah", "Created with python and love<3 !", "orange", "thing", "temperature", "negotiation", "disk", "haha"]

print("start")
time.sleep(2)
x=1
x=x+1

print(x)
while x <=100:
    b = random.choice(a)
    print(b)
    c = pyperclip.copy(b)
    print(c)
    x=x+1
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    print(x)
