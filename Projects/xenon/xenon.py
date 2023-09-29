from tkinter import *
from abc import ABC , abstractmethod

win=Tk()

class Window:
    def __init__(self):
        self.width=500
        self.height= 500
        self.title="Xenon"

    def window_res(self):
        win.geometry("500x500")
        win.maxsize(self.width, self.height)
        win.minsize(self.width, self.height)
        win.title(self.title)
        win.configure(bg="#FFFFFF")

class Win_frames(ABC):
    def frames_gen(self, k, bd, wd, ht):
        flist=[]
        for i in range(k+1):
            flist.append(Frame(win, bg="#808080" ,borderwidth=bd, relief=SUNKEN, width=wd, height=ht))
        return flist

    @abstractmethod
    def frames_pos(self):
        pass


class AuthWindow(Window,Win_frames):
    def __init__(self):
        Window().__init__()
        Window().window_res()
    

    def frames_pos(self):
        y= self.frames_gen(1,1,400,400)
        y[0].pack(side="top", expand=False)
        print("Frame positioned")
        Button(y[0], text="Sign In", bg="#FFFFFF", command= lambda: self.auth_script()).pack()


    def auth_script(self):
        #Auth-Script
        print("Executing-Auth-Script")
        pass



if __name__=="__main__":
    AuthWindow().frames_pos()
    win.mainloop()

