import os
import time
import random
q = input("Do you have pyautogui and pyperclip installed? (type y / n / ns (not sure)) : ")
w = q.lower()
if w == 'y':
    print("Let's proceed!")
elif w == 'n':
    print("Just stay connected to internet!")
    time.sleep(2)
    os.system('pip install pyperclip')
    os.system('pip install pyautogui')
    print("\n We are ready to go!")
elif w == 'ns':
    print("Just stay connected to internet!")
    time.sleep(2)
    os.system('pip install pyperclip')
    os.system('pip install pyautogui')
    print("\n We are ready to go!")
else:
    print("Invalid input!")
print("\n")
import pyperclip #pip install pyperclip
import pyautogui #pip install pyautogui

a = []
while True:
    user_input = input("Enter a value (press 'q' to quit): ")
    if user_input == "q":
        break
    a.append(user_input)
print(a)
zz = input("Are these you want?(y/n) ")
z = zz.lower()
if z == "y":
    print("Let's go to the next step.")
else:
    a = []
    while True:
        user_input = input("Enter a value (press 'q' to quit): ")
        if user_input == "q":
            break
        a.append(user_input)
    print(a)

#Taking inputs
y = int(input("How many messages to send : "))
print(y, "messages will be send in 3 sec.\nOpen any chat fast.")
time.sleep(1)
print('2')
time.sleep(1)
print('1')
time.sleep(1)
#

if y > 3000:
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
