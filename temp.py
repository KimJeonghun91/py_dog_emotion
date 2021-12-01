import tkinter as tk
from tkinter import filedialog as fd
import cv2
import sys
from tkinter import messagebox as mb

image = 0
img_gray = 0
filename = ''
img_bin = 0
img_canny_edge = 0

def file_open():
    global image,filename # 선언문이 없어서 지역변수, 전역변수 구분이 안되기때문에 전역 변수 사용을 명시함
    
    filename = fd.askopenfilename()
    print(filename)
    image = cv2.imread(filename)
    cv2.imshow(filename, image)

    
def convert_gray():
    global image, img_gray, filename

    if type(image) is int: 
        print('이미지가 없음')
        mb.showerror('이미지 없음')
    else:
        img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imshow('convert_gray', img_gray)

    
def binarization():
    global img_gray, filename, img_bin
    
    if type(img_gray) is int: 
        print('img_gray가 없음')
        mb.showerror('img_gray가 없음')
    else:
        _, img_bin = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
        cv2.imshow('binarization',img_bin)

    
def canny_edge():
    global img_gray, filename, img_canny_edge
    
    if type(img_gray) is int: 
        print('img_gray가 없음')
        mb.showerror('img_gray가 없음')
    else:
        img_canny_edge = cv2.Canny(img_gray, 100, 200)
        cv2.imshow('Canny Edge', img_canny_edge)
    
    
def quit_program():
    cv2.destroyAllWindows()
    sys.exit()
    
    


window = tk.Tk()
window.title("assignment")

btn_file_open = tk.Button(window, width=40, padx=5, pady=5, text='File Open...', command=file_open)
btn_file_open.grid(row=0, column=0, sticky=tk.EW)

btn_gray = tk.Button(window, padx=5, pady=5, text='Gray Conversion', command=convert_gray)
btn_gray.grid(row=1, column=0, sticky=tk.EW)

btn_binarize = tk.Button(window, padx=5, pady=5, text='Binarization', command=binarization)
btn_binarize.grid(row=2, column=0, sticky=tk.EW)

btn_edge = tk.Button(window, padx=5, pady=5, text='Canny Edge', command=canny_edge)
btn_edge.grid(row=3, column=0, sticky=tk.EW)

btn_end_program = tk.Button(window, padx=5, pady=5, text='Exit', command=quit_program)
btn_end_program.grid(row=4, column=0, sticky=tk.EW)


window.mainloop()