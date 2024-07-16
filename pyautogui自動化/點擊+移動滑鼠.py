import pyautogui

button = 'left', 'middle', 'right'


#在(width, height)點擊滑鼠(預設左鍵)
while True:
    pyautogui.click(15,1056)
    #點擊滑鼠左鍵
    pyautogui.click(132,751, button='left')
