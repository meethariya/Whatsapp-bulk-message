import pyautogui as pg
import webbrowser as web
import time
import pandas as pd

# reading csv file to get list of numbers and their message
data = pd.read_csv("numbers.csv")
data_dict = data.to_dict('list')
num = data_dict['number']
messages = data_dict['Message']
combo = zip(num,messages)
for num,message in combo:
    web.open("https://web.whatsapp.com/send?phone="+str(num)+"&text="+message)
    # wait till the image is found on screen so that program can wait till site is loaded
    while True:
        logo=pg.locateOnScreen("Screenshot (102).png")
        if logo is not None:
            break
    width,height = pg.size()
    # click on center of screen
    pg.click(width/2,height/2)
    time.sleep(1)
    pg.press('enter')
    # wait for message being sent
    time.sleep(4)
    # close the tab
    pg.hotkey('ctrl', 'w')