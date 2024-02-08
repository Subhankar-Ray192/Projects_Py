#Calculator

import tkinter as container
import re

from tkinter import *
from tkinter.font import Font
from tkinter import ttk


windObj=container.Tk(className="Calculator",useTk=1)
windObj.title("Calculator")
windObj.grid_columnconfigure((0,1,2,3),weight=1,uniform="column")


menu=["Simplistic","Scienctific","History"]
operators=["/","*","+","-","%"]
number=["1","2","3","4","5","6","7","8","9","0"]
extraChar=["C","=","(",")","x"]
colorPalette=["#ffffff","#f0f8ff","#b0d0ed","#8fd3fe","#6ac5ef","#b5e2ff","#296d98","#FFDF00","#000000"]
fontList=[(Font(family="Calibri",size=12)),(Font(family="Calibri",size=15)),(Font(family="Calibri",size=17,weight="bold"))]

mainFrame=Frame(windObj,bg=colorPalette[1],highlightbackground=colorPalette[1],highlightthickness=0,height=542,width=402)
menuFrame=Frame(windObj,bg=colorPalette[1],highlightbackground=colorPalette[1],highlightthickness=0,height=30,width=4010)

class Windows:
 
  
  def __init__(self):
   self.height=413
   self.width=428

  def layout(self):
   '''Fixes the Windows Layout'''

   windObj.minsize(self.width,self.height)
   windObj.maxsize(self.width,self.height)
   windObj.config(bg=colorPalette[1])
  
  def quit(self):
   windObj.destroy()
  
  def mainkeyControls(self):
   windObj.bind("<Control-q>",lambda event: quit())


class Component:
  
  
  def __init__(self):
   #objF: Frame_Objects List
   self.objF=[] 
  
  
  def frameGen(self):
   '''Generation of Frames(5)'''
   
   for i in range(6):
    self.objF.append(Frame(mainFrame,bg=colorPalette[1],highlightbackground=colorPalette[1],highlightthickness=0,width=400,height=80))
  
  
  def entry(self,wd):
   '''Places Entry Objects on Window Grid Layout'''
   
   #eObj: Entry Object
   global eObj
   
   #Object: Created
   eObj=Entry(self.objF[0],width=wd,borderwidth=0,font=fontList[1],exportselection=1,bg=colorPalette[1])
   eObj.grid(row=0,column=0,columnspan=4,padx=0,pady=10)
   
   #Object: Placed
   self.objF[0].grid(row=0,column=0,columnspan=4)

  
  
  def buttonFrame(self):
   '''Places Button Object on Child Frames'''

   #obj: Button Object List
   obj=[] 

   #Object->Frame_1: Created
   obj.append(Button(self.objF[1],text=number[0],padx=45,pady=18,command= lambda: self.input(number[0]),bg=colorPalette[1],activebackground=colorPalette[2],font=fontList[0],relief=GROOVE))
   obj.append(Button(self.objF[1],text=number[1],padx=45,pady=18,command= lambda: self.input(number[1]),bg=colorPalette[1],activebackground=colorPalette[2],font=fontList[0],relief=GROOVE))
   obj.append(Button(self.objF[1],text=number[2],padx=45,pady=18,command= lambda: self.input(number[2]),bg=colorPalette[1],activebackground=colorPalette[2],font=fontList[0],relief=GROOVE))
   obj.append(Button(self.objF[1],text=number[9],padx=45,pady=18,command= lambda: self.input(number[9]),bg=colorPalette[1],activebackground=colorPalette[2],font=fontList[0],relief=GROOVE))
   
   #Object->Frame_2: Created
   obj.append(Button(self.objF[2],text=number[3],padx=45,pady=18,command= lambda: self.input(number[3]),bg=colorPalette[1],activebackground=colorPalette[2],font=fontList[0],relief=GROOVE))
   obj.append(Button(self.objF[2],text=number[4],padx=45,pady=18,command= lambda: self.input(number[4]),bg=colorPalette[1],activebackground=colorPalette[2],font=fontList[0],relief=GROOVE))
   obj.append(Button(self.objF[2],text=number[5],padx=45,pady=18,command= lambda: self.input(number[5]),bg=colorPalette[1],activebackground=colorPalette[2],font=fontList[0],relief=GROOVE))
   obj.append(Button(self.objF[2],text=extraChar[0],padx=45,pady=18,command=lambda: self.clear(),bg=colorPalette[1],activebackground=colorPalette[2],font=fontList[0],relief=GROOVE))
   
   #Object->Frame_3: Created
   obj.append(Button(self.objF[3],text=number[6],padx=45,pady=18,command= lambda: self.input(number[6]),bg=colorPalette[1],activebackground=colorPalette[2],font=fontList[0],relief=GROOVE))
   obj.append(Button(self.objF[3],text=number[7],padx=45,pady=18,command= lambda: self.input(number[7]),bg=colorPalette[1],activebackground=colorPalette[2],font=fontList[0],relief=GROOVE))
   obj.append(Button(self.objF[3],text=number[8],padx=45,pady=18,command= lambda: self.input(number[8]),bg=colorPalette[1],activebackground=colorPalette[2],font=fontList[0],relief=GROOVE))
   obj.append(Button(self.objF[3],text=operators[0],padx=45,pady=18,command= lambda: self.input(operators[0]),bg=colorPalette[1],activebackground=colorPalette[2],font=fontList[0],relief=GROOVE))
   
   #Object->Frame_4: Created
   obj.append(Button(self.objF[4],text=operators[1],padx=45,pady=18,command= lambda: self.input(operators[1]),bg=colorPalette[1],activebackground=colorPalette[2],font=fontList[0],relief=GROOVE))
   obj.append(Button(self.objF[4],text=operators[2],padx=45,pady=18,command= lambda: self.input(operators[2]),bg=colorPalette[1],activebackground=colorPalette[2],font=fontList[0],relief=GROOVE))
   obj.append(Button(self.objF[4],text=operators[3],padx=47,pady=18,command= lambda: self.input(operators[3]),bg=colorPalette[1],activebackground=colorPalette[2],font=fontList[0],relief=GROOVE))
   obj.append(Button(self.objF[4],text=extraChar[1],padx=45,pady=18,command= lambda: RPN().output(eObj),bg=colorPalette[1],activebackground=colorPalette[2],font=fontList[0],relief=GROOVE))
   
   #Object->Frame_5: Created
   obj.append(Button(self.objF[5],text=extraChar[2],padx=47,pady=18,command=lambda: self.input(extraChar[2]),bg=colorPalette[1],activebackground=colorPalette[2],font=fontList[0],relief=GROOVE))   
   obj.append(Button(self.objF[5],text=extraChar[3],padx=47,pady=18,command=lambda: self.input(extraChar[3]),bg=colorPalette[1],activebackground=colorPalette[2],font=fontList[0],relief=GROOVE))
   obj.append(Button(self.objF[5],text=operators[4],padx=43,pady=18,command= lambda: self.input(operators[4]),bg=colorPalette[1],activebackground=colorPalette[2],font=fontList[0],relief=GROOVE))
   obj.append(Button(self.objF[5],text=extraChar[4],padx=45,pady=18,command=lambda: self.cross(),bg=colorPalette[1],activebackground=colorPalette[2],font=fontList[0],relief=GROOVE))   
   
   #Button Object List Pointer
   bObj_ptr=1
   
   #Object: Placed
   for i in range(5):
     for j in range(4):
       obj[bObj_ptr-1].grid(row=0,column=j)
       bObj_ptr=bObj_ptr+1
     self.objF[i+1].grid(row=(i+1),column=0,columnspan=3,sticky=W)
   
   #Grid placed on Main Frame
   mainFrame.grid(row=1,column=0,columnspan=3,rowspan=6)
   
  def clear(self):
   '''Clearing Entry Text'''
   
   eObj.delete(0,END)  
  
  def keyControls(self):
   windObj.bind("<Control-x>",lambda event: self.cross())
  
  def input(self,prev_txt):
   '''Gettting Text Input from Entry Object'''
   
   curr_txt=str(eObj.get())
   self.clear() 
   eObj.insert(0,curr_txt+prev_txt)

  def cross(self):
   '''Deleted 1 Character in Reverse from Text'''
   
   curr_txt=str(eObj.get())[:-1]
   self.clear()
   eObj.insert(0,curr_txt)
    
  def compEvent(self):
   '''Main Controller Event for Layout, Calling each function'''
   
   self.frameGen()
   self.entry(40)
   self.buttonFrame()
   self.keyControls()




class RPN:

  def __init__(self):
   self.curr_pos=0
   self.curr_token=None
   self.result=0

  def output(self,eObj):
   '''Displays output on the entry'''

   self.getTokens(eObj.get()) 
   eObj.delete(0,END)
   eObj.insert(0,self.result)
   
  def getTokens(self,entry):
   '''Digit,Operator,Parenthesis extraction'''
   
   entry = re.findall(r'\d+|\+|\-|\*|\/|\(|\)', entry)
   self.result = self.token_E(entry)

  def token_E(self,token):
   '''Expression Evaluation'''
   
   self.curr_token = token[self.curr_pos]
   result = self.token_T(token)
   
   while(self.curr_token in ("-","+")):
    
    opt_ptr = self.curr_token
    self.consume_token(token)
    term = self.token_F(token)
    
    if(opt_ptr == "+"):
      result += term
    else:
      result -= term
   
   return result 
  
  def token_T(self,token):
   '''Term Evaluation'''
   result = self.token_F(token)
   
   while(self.curr_token in ("/","*","%")):
    
    opt_ptr = self.curr_token
    self.consume_token(token)
    factor = self.token_T(token)
    
    if(opt_ptr == "/"):
      result /= factor
    elif(opt_ptr == "%"):
      result %= factor
    else:
      result *= factor
   
   return result 

  def token_F(self,token):
    '''Factor Evaluation'''
    
    if(self.curr_token == "("):
     self.consume_token(token)
     result=self.token_E(token)
     self.consume_token(token)
    else:
     result = int(self.curr_token)
     self.consume_token(token)
    
    return result
   
  def consume_token(self, token):
    self.curr_pos += 1
    if self.curr_pos < len(token):
       self.curr_token = token[self.curr_pos]
  
class Menu:
  
  def __init__(self):
    return

  def option(self):
    inp=StringVar()
    om=ttk.OptionMenu(menuFrame,inp,menu[0],*menu)
    style=ttk.Style()
    style.configure("TMenubutton",background=colorPalette[1],selectbackground=colorPalette[2],foreground="#000000",highlightthickness=0,bd=0,font=fontList[2])
    om["menu"].config(relief=FLAT,borderwidth=1,activeborderwidth=2,activebackground=colorPalette[2],bg=colorPalette[1],selectcolor=colorPalette[1],activeforeground=colorPalette[8])
    om.pack(side=LEFT)
      
  def menuEvent(self):
    self.option()
    menuFrame.grid(row=0,column=2,columnspan=3)
    

def mainWindow():
 Windows().layout() 
 Windows().mainkeyControls()
 Menu().menuEvent()
 Component().compEvent()
 windObj.mainloop()


mainWindow()