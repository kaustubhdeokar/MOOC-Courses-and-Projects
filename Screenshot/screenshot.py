import time
import cv2
import pyautogui
import numpy as np
import sys

def main():
    while(True):
        image = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
        save_as = str(time.time())+".png"
        cv2.imwrite("./images/image"+save_as,image)
        print("image "+ save_as + " saved successfully.")
        time.sleep(int(sys.argv[1]))
        

main()
    
