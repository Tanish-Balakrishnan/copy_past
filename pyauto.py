import time
import pyautogui
str=input("Enter the file location :")
f = open(str, "r")
time.sleep(10)
pyautogui.write((f.read()))
