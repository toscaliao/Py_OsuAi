import pyautogui
import os
import dxcam
import torch
import psutil
import sys
import pyautogui as m
import keyboard
import asyncio

def close():
    pyautogui.hotkey("alt",'f4')

def clear_console():
    os.system('cls')

def get_fps(cuda_available):
    if (cuda_available):
        fps = 177
    else:
        fps = 60
    return fps

def camera_set(fps):
    camera = dxcam.create()
    camera.start(target_fps = fps)
    return camera

def device_check():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print("CPU count:",psutil.cpu_count())
    print("virtual memory:",psutil.virtual_memory())  
    return device

def writeline(a):
    sys.stdout.write(a)
    sys.stdout.flush()

def countdown(start,end):
    import time
    for i in range(end,start,-1):
            writeline(str(i))
            writeline(" ")
            time.sleep(1)
    clear_console()

def detection(camera,model,width,height,x,y,x1,y1):
    Screenshot = camera.get_latest_frame()
    circles = model.predict(Screenshot)
    if (len(circles[0].boxes.xyxy) != 0):
        try:
            x1 = int(circles[0].boxes.xyxy[0][0])
            y1 = int(circles[0].boxes.xyxy[0][1])
        except:
            x1, y1 = width/2, height/2
    x1 = x * x1
    y1 = y * y1
    m.moveTo(x1, y1,duration=0.01)


def detect_kb():
    if keyboard.is_pressed('1'):
            if (sys.platform == "win32" or sys.platform == "win64"):
                clear_console()
                print('\nSee you next time.\n')
                exit()
    elif keyboard.is_pressed("2"):
        while True:
            if keyboard.is_pressed("3"):
                clear_console()
                break


async def detection_async(camera,model,width,height,x,y,x1,y1):
    Screenshot = camera.get_latest_frame()
    circles = model.predict(Screenshot)
    if (len(circles[0].boxes.xyxy) != 0):
        try:
            x1 = int(circles[0].boxes.xyxy[0][0])
            y1 = int(circles[0].boxes.xyxy[0][1])
        except:
            x1, y1 = width/2, height/2
    x1 = x * x1
    y1 = y * y1
    await asyncio.sleep(0.01)
    m.moveTo(x1, y1)

def asynctest(device):
    if (device == 'gpu'):
        asynct = 2
    else:
        asynct = 4
    return asynct

