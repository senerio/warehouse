import pyautogui
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import pytesseract
import cv2
import numpy

def checkGameResolution():
    window = pyautogui.getWindowsWithTitle('Reverse: 1999')
    if not window:
        print('window does not exist')
    elif window[0].size > (1366+100, 768+100):
        print('wrong resolution. go to Menu > Setting > Graphics > Resolution > 1366*768')
    else:
        return
    exit()
    # else:
        # image = Image.open('tile-23.png')
        # image.resize([int(d * scale) for d in image.size])
        # item = pyautogui.locateCenterOnScreen(image, confidence=0.8)
        # pyautogui.moveTo(item)
checkGameResolution()

pytesseract.pytesseract.tesseract_cmd = r'./tesseract/tesseract.exe'


def getItemCount(file):
    image = Image.open('tile-%s.png' % file)
    itemLocation =  pyautogui.locateOnScreen(image, confidence=0.9)
    region = (
        itemLocation.left + 40,
        itemLocation.top + itemLocation.height + 2,
        itemLocation.width - 40*2,
        20 - 2
    )
    #pyautogui.moveTo(region)
    image = pyautogui.screenshot(region=[int(i) for i in region])
    image = image.resize([int(i*2) for i in image.size])
    #imageCount = pyautogui.screenshot('test.png', region=[int(i) for i in region])
    #print(imageCount)
    # img = cv2.imread("temp2.png")
    img = numpy.array(image)
    gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thr = cv2.threshold(gry, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    
    cv2.imwrite('temp2.png', thr)
    count = pytesseract.image_to_string(thr, config='--psm 6 -c tessedit_char_whitelist=0123456789').strip()
    print(file + ': ' + count)

getItemCount('0')
getItemCount('1')
getItemCount('2')
getItemCount('3')
getItemCount('4')
getItemCount('5')
getItemCount('6')
getItemCount('7')
getItemCount('8')
getItemCount('9')
getItemCount('10')
getItemCount('11')

# save image. 128x99. +99 from bottom. max 128 from left.

# find count
#print(pytesseract.image_to_string(Image.open('1.png'), config='--psm 6 -c tessedit_char_whitelist=0123456789'))