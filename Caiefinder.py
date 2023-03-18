import webbrowser
import pyautogui as pag
import time

sleep = time.sleep

def meow():
    if ' ' in z or 'a' in z:
        webbrowser.open("https://caiefinder.com/")
        pag.click(892,10)
        sleep(0.5)
        pag.click(954,271)
        pag.click(937,344)
        sleep(1)
        pag.doubleClick(748,320)
        sleep(1)
        pag.typewrite(z)
        pag.press('enter')
print("Enter details")
z = input()

meow()

