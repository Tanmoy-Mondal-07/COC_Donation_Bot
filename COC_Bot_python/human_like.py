import pyautogui
import random
import time
import math

def sigmoid(t):
    return 1 / (1 + math.exp(-t))

def human_like_move(x, y, duration):
    
    start_x, start_y = pyautogui.position()

    control_x1 = start_x + (x - start_x) * random.uniform(0.1, 0.3)
    control_y1 = start_y + (y - start_y) * random.uniform(0.1, 0.3)
    control_x2 = start_x + (x - start_x) * random.uniform(0.7, 0.9)
    control_y2 = start_y + (y - start_y) * random.uniform(0.7, 0.9)

    steps = random.randint(50, 100)
    for i in range(steps):
        t = i / steps
        t_accel = sigmoid((t - 0.5) * 12)  

        intermediate_x = (1 - t_accel)**3 * start_x + 3 * (1 - t_accel)**2 * t_accel * control_x1 + 3 * (1 - t_accel) * t_accel**2 * control_x2 + t_accel**3 * x
        intermediate_y = (1 - t_accel)**3 * start_y + 3 * (1 - t_accel)**2 * t_accel * control_y1 + 3 * (1 - t_accel) * t_accel**2 * control_y2 + t_accel**3 * y

        intermediate_x += random.uniform(-3, 3)
        intermediate_y += random.uniform(-3, 3)

        pyautogui.moveTo(intermediate_x, intermediate_y, duration=0.01)
        time.sleep(random.uniform(0.01, 0.03))

    pyautogui.moveTo(x, y, duration=random.uniform(0.1, 0.3))

def click(target):
    
    x,y=target
    human_like_move(x, y, duration=random.uniform(1.0, 2.0))
    time.sleep(random.uniform(0.2, 0.5))  
    pyautogui.mouseDown()
    time.sleep(random.uniform(0.1, 0.3))  
    pyautogui.mouseUp()
    time.sleep(random.uniform(0.2, 0.5))  

