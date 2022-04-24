import pyautogui as pag

savepath = './test/image_1.png'

icon_loc = pag.locateOnScreen(savepath)
x, y = pag.center(icon_loc)

pag.moveTo(x, y, 1)
pag.doubleClick(x, y)