#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Developer Muhammad Zubair


import pyautogui       #Must import pyautogui() using pip install pyautogui   
import time
time.sleep(3)   #Sleep will give you a time to move your cursor where you want
count =0;
while count<=5:        #Enter number of count (Number of time you want to send message)
    pyautogui.typewrite(f"Aya Maza{count}")       #Enter any thing that you want to send (Put it in the .typwritr(?))
    pyautogui.press("enter")
    count=count+1
pyautogui.typewrite("Loop Developed By ZJ Developer") 
pyautogui.press("enter") 

#When you start this program the place where you cursor is it will print data the counts you want