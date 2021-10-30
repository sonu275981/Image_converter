Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:13:57) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import *   
  
  
top = Tk()  
  
top.geometry("200x100")  
  
b = Button(top,text = "Simple")  
  
b.pack()  
  
top.mainaloop()  
