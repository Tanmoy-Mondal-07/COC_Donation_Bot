# # im=pyautogui.screenshot()
# # pxl=im.getpixel((200,200))
# # print(pxl)
# a = pyautogui.locateCenterOnScreen('02.png',region=(0,0,900,1070))
# click(a) #1900,1070

import pyautogui
import cv2
import time
import numpy as np
import threading
from draw import draw_square
from human_like import click


def screenshotx(x,y,wi,hi):
    region=(x,y,wi,hi)
    screenshot = pyautogui.screenshot(region=region)
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    return (screenshot_gray)

# Function to find template image in the screenshot
def re_zero():
    while True:
        def donate_go(i):
            status, top,left, bottom_right = find_template((f'donate_file/{i}'),1200,50,400,450)
            print("try_",i[:-4])
            if status is True:
                print(i[:-4],"found at:", top,left, bottom_right)
                click(bottom_right)
                print(i[:-4],"donated")
                status, top_a,left_a, bottom_right = find_template(i,950,50,400,450)
                if status is True:
                    donate_go(i)
                else:
                    tar=(1700,200)
                    click(tar)
                    
            else:
                print(i[:-4],"isn't available or.....")
                tar=(1700,200)
                click(tar)
                

        def find_template(template_path,x,y,wi,hi):
            t2=threading.Thread(target=draw_square, args=[x,y,wi,hi])
            t2.start()
            t2.join()
            # draw_square(x,y,wi,hi)
            screenshot=screenshotx(x,y,wi,hi)
            template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)  # Load template as grayscale
            w, h = template.shape[::-1]

            res = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
            threshold = 0.7
            loc = np.where(res >= threshold)

            if len(loc[0]) > 0:
                return True, (loc[1][0]+x),(loc[0][0]+y), (loc[1][0]+x+ w/2, loc[0][0]+y+ h/2)
            else:
                return False, None, None,None


        template_path = 'donate.png'
        template_arr = ['loon.png','light.png','blimp.png','boom.png','clon.png','fzz.png','invis.png','sup.png']


        for i in template_arr:
            for j in range(1):
                status, top_a,left_a, bottom_right = find_template(i,950,50,400,450)
                print("try_req_",i[:-4])
                if status is True:
                    print(i[:-4],"_req_found")
                    donate, top,left, bottom_right = find_template(template_path,int(top_a),int(left_a),400,100)
                    if donate:
                        print("req found at:", top,left, bottom_right)
                        click(bottom_right)
                        donate_go(i)
                    else:
                        print("donate button not found")
                else:
                    print(i[:-4],"req not found")
        time.sleep(5)

t1=threading.Thread(target=re_zero)
t1.start()
t1.join()

