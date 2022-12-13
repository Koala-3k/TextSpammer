import pyautogui as koala
import time

x = input("spam text: ")
y = int(input("how many times: "))
print("get to the window, starting in 10 seconds, get your cursor in the chatbox or you will regret it.")
time.sleep(10) #time in which u want it to start spamming. Decresing this from 10s may have severe consequences.
for i in range(y):
    time.sleep(1) #change this accoring to the rate limit
    koala.typewrite(x)
    koala.press("ENTER")