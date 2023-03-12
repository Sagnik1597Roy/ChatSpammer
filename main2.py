import os
import time
import random
import pyperclip #pip install pyperclip
import pyautogui #pip install pyautogui

# Some random words. You may change them according to your needs.
# Just keep the double quotes intact
# Add as many words as you wish
a = ["Hello", "Hi", "Created with python and love<3!"]
#


#Taking inputs
print("\n")
e = str(input("Do you want to change the words? \n(type y / n): "))
r = e.lower()
if r == 'y':
    print("Change the variable 'a' in the python program. \nOpen it by right-clicking it and opening it with notepad. \nAdd anything but withing INVERTED COMMAS")
elif r == 'n':
    print("Let's go ahead!")
else:
    print("Invalid input!")
print("\n")
#
q = input("Do you have pyautogui and pyperclip installed? (type y / n / ns (not sure)) : ")
w = q.lower()
if w == 'y':
    print("Let's proceed!")
elif w == 'n':
    os.system('pip install pyperclip')
    os.system('pip install pyautogui')
    print("\n We are ready to go!")
elif w == 'ns':
    os.system('pip install pyperclip')
    os.system('pip install pyautogui')
    print("\n We are ready to go!")
else:
    print("Invalid input!")
print("\n")
#
y = int(input("How many messages to send : "))
print(y, "messages will be send in 3 sec.\nOpen any chat fast.")
time.sleep(1)
print('2')
time.sleep(1)
print('1')
time.sleep(1)
#

if y > 999:
    print("Really large number!")
else:
    print("start")
    x=1
    print(x)

    while x <= y:
        b = random.choice(a)
        print(b)
        c = pyperclip.copy(b)
        x=x+1
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        print(x)
