from PIL import Image
from PIL import ImageChops
import folder

def gdje(pomak,pomak2):
    dir=folder.get()
    im = Image.open(dir+'slika.jpg')

    size=(714-pomak2,441+pomak,731-pomak2,452+pomak) #povecat za 1 kad bude trebalo
    im2=im.crop(size) 
    im3=im2.convert('P').convert('1')
    pix = im3.load()
    im3.save(dir+'gumb6.jpg') #button6
    
    a=0
    for i in range(17):
        for j in range(11):
            if pix[i,j]>0:
               a+=1
            
    if a>50:
        #print('button na poziciji 6')
        return (6)
    a=0
    size=(307-pomak2,441+pomak,324-pomak2,452+pomak) #povecat za 1 kad bude trebalo
    im2=im.crop(size) 
    im3=im2.convert('P').convert('1')
    pix = im3.load()
    im3.save(dir+'gumb1.jpg') #button1
    
    for i in range(17):
        for j in range(11):
            if pix[i,j]>0:
               a+=1

    if a>50:
        #print('button na poziciji 1')
        return (1)
    a=0
    
    size=(145-pomak2,346+pomak,162-pomak2,357+pomak) #povecat za 1 kad bude trebalo
    im2=im.crop(size) 
    im3=im2.convert('P').convert('1')
    pix = im3.load()
    im3.save(dir+'gumb2.jpg') #button2
    
    for i in range(17):
        for j in range(11):
            if pix[i,j]>0:
               a+=1

    if a>50:
        #print('button na poziciji 2')
        return (2)
    a=0
    
    size=(171-pomak2,222+pomak,188-pomak2,233+pomak) #povecat za 1 kad bude trebalo
    im2=im.crop(size) 
    im3=im2.convert('P').convert('1')
    pix = im3.load()
    im3.save(dir+'gumb3.jpg') #button3

    for i in range(17):
        for j in range(11):
            if pix[i,j]>0:
               a+=1

    if a>50:
        #print('button na poziciji 3')
        return (3)
    a=0

    size=(844-pomak2,222+pomak,861-pomak2,233+pomak) #povecat za 1 kad bude trebalo
    im2=im.crop(size) 
    im3=im2.convert('P').convert('1')
    pix = im3.load()
    im3.save(dir+'gumb4.jpg') #button4

    for i in range(17):
        for j in range(11):
            if pix[i,j]>0:
               a+=1

    if a>50:
        #print('button na poziciji 4')
        return (4)
    a=0

    size=(870-pomak2,344+pomak,887-pomak2,355+pomak) #povecat za 1 kad bude trebalo
    im2=im.crop(size) 
    im3=im2.convert('P').convert('1')
    pix = im3.load()
    im3.save(dir+'gumb5.jpg') #button5

    for i in range(17):
        for j in range(11):
            if pix[i,j]>0:
               a+=1

    if a>50:
        #print('button na poziciji 5')
        return(5)
    a=0
