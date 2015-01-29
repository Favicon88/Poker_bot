from PIL import ImageGrab
import time
from PIL import Image
from PIL import ImageChops
import folder
import win32gui

def grabi(pomak,pomak2):
    dir=folder.get()
    toplist, winlist = [], []
    def enum_cb(hwnd, results):
        winlist.append((hwnd, win32gui.GetWindowText(hwnd)))
    win32gui.EnumWindows(enum_cb, toplist)

    firefox = [(hwnd, title) for hwnd, title in winlist if '$0.01' in title.lower()]
    # just grab the hwnd for first window matching firefox
    firefox = firefox[0]
    hwnd = firefox[0]
    win32gui.SetForegroundWindow(hwnd)
    win32gui.MoveWindow(hwnd, 0, 0, 1028, 734, True)
    bbox = win32gui.GetWindowRect(hwnd)
    time.sleep(4)
    img = ImageGrab.grab(bbox)
    img.save(dir+'slika.jpg','JPEG')
    

    #time.sleep(4)
    #img = ImageGrab.grab()

    #img.save(dir+'slika.jpg','JPEG')
    im1 = Image.open(dir+'slika.jpg')

    size=(456,594,462,610)
    im2=im1.crop(size)
    im2.save(dir+'pomak.jpg','JPEG')

    size=(326,594,348,599)
    im2=im1.crop(size)
    im2.save(dir+'pomak2.jpg','JPEG')


    size=(741-pomak2,438+pomak,761-pomak2,480+pomak)
    im2=im1.crop(size)
    im2.save(dir+'1.jpg','JPEG')

    size1=(801-pomak2,438+pomak,821-pomak2,480+pomak)
    im2=im1.crop(size1)
    im2.save(dir+'2.jpg','JPEG')

    size2=(358-pomak2,233+pomak,378-pomak2,275+pomak)
    im2=im1.crop(size2)
    im2.save(dir+'3.jpg','JPEG')

    size3=(423-pomak2,233+pomak,443-pomak2,275+pomak)
    im2=im1.crop(size3)
    im2.save(dir+'4.jpg','JPEG')

    size4=(488-pomak2,233+pomak,508-pomak2,275+pomak)
    im2=im1.crop(size4)
    im2.save(dir+'5.jpg','JPEG')

    size5=(553-pomak2,233+pomak,573-pomak2,275+pomak)
    im2=im1.crop(size5)
    im2.save(dir+'6.jpg','JPEG')

    size6=(618-pomak2,233+pomak,638-pomak2,275+pomak)
    im2=im1.crop(size6)
    im2.save(dir+'7.jpg','JPEG')

    size7=(713-pomak2,665+pomak,823-pomak2,721+pomak)
    im2=im1.crop(size7)
    im2.save(dir+'8.jpg','JPEG')

    size8=(883-pomak2,665+pomak,993-pomak2,721+pomak)
    im2=im1.crop(size8)
    im2.save(dir+'9.jpg','JPEG')


    size9=(253-pomak2,60+pomak,273-pomak2,102+pomak)
    im2=im1.crop(size9)
    im2.save(dir+'10.jpg','JPEG')

    size10=(723-pomak2,60+pomak,743-pomak2,102+pomak)
    im2=im1.crop(size10)
    im2.save(dir+'11.jpg','JPEG')


















    
