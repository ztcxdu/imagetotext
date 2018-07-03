#coding=utf8  
from PIL import Image  

IMG = 'test.jpg'  
WIDTH = 160  
HEIGHT = 80  
OUTPUT = 'test.txt'  
  
ascii_char = list("$@B%8&WM#oahkbdpqwmZ*O0QLCJUYXzcvunxrjft/\|()1{}[]<>?-_+~i!lI;:,\"^`'. ")  
    
def get_char(r,g,b,alpha = 256):  
    if alpha == 0:  
        return ' '  
    length = len(ascii_char)  
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)  
  
    unit = (256.0 + 1)/length  
    return ascii_char[int(gray/unit)]  
  
if __name__ == '__main__':  
  
    im = Image.open(IMG)
    #im=im.transpose(Image.ROTATE_180)  
    im = im.resize((WIDTH,HEIGHT), Image.NEAREST)  
    #im.show()
    txt = ""  
  
    for i in range(HEIGHT):  
        for j in range(WIDTH):  
            txt += get_char(*im.getpixel((j,i)))  
        txt += '\n'  
  
    print(txt)  
    
    if OUTPUT:  
        with open(OUTPUT,'w') as f:  
            f.write(txt)  
    else:  
        with open("output.txt",'w') as f:  
            f.write(txt) 
