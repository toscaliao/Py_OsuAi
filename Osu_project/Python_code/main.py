# 模組導入(之後再把沒用到的清一清)
import pyautogui as m
import time as t
import keyboard
from ultralytics import YOLO as v8  #YOLOV8
import sys 
from PIL import Image
import torch
import threading #still developing 
import pathlib
import UI
import osuai_function_list as o
import asyncio 
x,y = None,None


#still developing
'''
UI.gui("osu",400,400) 
'''

#dxcam函式的設定
fps = o.get_fps(torch.cuda.is_available())
camera = o.camera_set(fps)

# 檢查GPU是否可用&性能測試
device = o.device_check()

#設定存放位置的路徑&設定模型路徑並讀取
path = pathlib.Path(__file__).parent.absolute().parent

#輸入模型版本並讀取
model = v8('yolov8n.pt')
model = v8(f"{path}/best_pt(Drop_here)/best.pt")
model.to(device)

#變數設置
m.FAILSAFE = False
Song_Not_End = True
x1,y1 = 0, 0
i = 0
circle_list = []

#讀取螢幕數據(長寬比)
screenx,screeny = m.size()
screenx = int(screenx)
screeny = int(screeny)
Screenshot = camera.get_latest_frame()
height, width = Screenshot.shape[:2]

#使用者協助調整倍率
img = Image.open(f'{path}/test_png/test_photo.png')
img.show()
print("This is a test ,for its multliplier,press 1 to continue")
first = t.time()
print("Time now: ",first)
while True:
    if keyboard.is_pressed("1"):
        x,y = m.position()
        Screenshot = camera.get_latest_frame()
        break
    elif ((t.time() - first) >= 60):
        import sys
        print("Overtime...")
        o.writeline("Exiting in: ")
        o.countdown(0,3)
        exit()

circles = model.predict(Screenshot)
o.close()

#設定xy座標
x = x / int(circles[0].boxes.xyxy[0][0])
y = y / int(circles[0].boxes.xyxy[0][1])

#印出x與y的倍率，方便觀察
print("x_multliper = ",x," y_multliper = ",y,"\n")

#WoP 是判斷使用者要使用的模式
WoP = str(input('Please choose the mode.\'w\' for writein,\'p\' for play\n'))

if (WoP == 'w'):
    print("The writein mode is starting.,",
          "\nPress 1 to end,",
          "\nPress 2 to pause,",
          "\npress 3 to continue")
    task = o.detection(camera,model,width,height,x,y,x1,y1)

    asynct = o.asynctest(device)

    while Song_Not_End:
        o.detection(camera,model,width,height,x,y,x1,y1)
        o.detect_kb()
        Screenshot = None

elif (WoP == 'p'):
    print('Still in progress.See you later :P')
    o.writeline("Ends in :")
    o.countdown(0,3)
    t.sleep(.5)
    exit()