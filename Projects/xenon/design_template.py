import pkg_resources
import subprocess

class Configure:
    def config_tk(self):
        print("Config-Chk")
        """
        # Check if python3-tk is already installed
        try:
            subprocess.run(["python3", "-c", "import tkinter"], check=True)
            print("python3-tk is already installed.")
        except subprocess.CalledProcessError:
            # If an error occurred, it means tkinter is not installed, so we'll try to install it
            try:
                subprocess.run(["sudo", "apt", "update"], check=True)
                subprocess.run(["sudo", "apt", "install", "-y", "python3-tk"], check=True)
                print("python3-tk has been installed.")
            except subprocess.CalledProcessError:
                print("Failed to install python3-tk. Please check your internet connection or try manually.")
                """

    def config_package(self,package_name):
        try:
            pkg_resources.get_distribution(package_name)
        except pkg_resources.DistributionNotFound:
            try:
                subprocess.check_call(["pip3", "install", package_name])
                print(f"{package_name} has been successfully installed.")
            except subprocess.CalledProcessError as e:
                print(f"Error installing {package_name}: {e}")

Configure().config_tk()
Configure().config_package(package_name = "multipledispatch")

import tkinter
from tkinter import *
from tkinter import ttk
from abc import ABC , abstractmethod
from multipledispatch import dispatch


win=Tk()


class SharedSpace:
    def set_height_width(self,height,width):
        self.height=height
        self.width=width

    def set_title(self,title):
        self.title = title


class DIFace:
    class ColorParameters(ABC): 
        @abstractmethod
        def color_loader(self):
            pass


class Window(SharedSpace):
    def __init__(self):
        super().set_height_width(500,500)
        super().set_title("Xenon")

    def set_res(self):
        win.geometry("500x500")
        win.maxsize(self.width, self.height)
        win.minsize(self.width, self.height)
        win.title(self.title)

class LIFace:
    class WinFrame(ABC,SharedSpace):
        @dispatch()
        def main_frame_gen(self):
            self.main_frame=Frame(win ,borderwidth=1 ,relief=SUNKEN ,width=self.width ,height=self.height)
            self.main_frame.pack(fill = BOTH, expand = True)
            self.main_frame.pack_propagate(0)
            self.main_frame.place(anchor = 'center', relx = 0.5, rely = 0.5)
            return self.main_frame

        @dispatch(int)
        def main_frame_gen(self,height_factor):
            self.main_frame=Frame(win ,borderwidth=1 ,relief=SUNKEN ,width=self.width ,height= self.height - height_factor)
            self.main_frame.pack(fill = BOTH, expand = True)
            self.main_frame.pack_propagate(0)
            self.main_frame.place(anchor = 'center', relx = 0.5, rely = 0.5)
            return self.main_frame
    
        @dispatch(int ,int ,int ,int ,str)
        def child_frame_gen(self, frame_count, borderwidth, height, width, color):
            gen_frame_list = []
            for i in range(1,frame_count+1):
                gen_frame_list.append(Frame(self.main_frame, bg=color ,borderwidth=borderwidth, relief=SUNKEN, width=width, height=height))
            return gen_frame_list
    
        @dispatch(int ,list ,int ,int ,int ,str)
        def child_frame_gen(self, frame_count, frame_list,  borderwidth, height, width, color):
            gen_frame_list=[]
            for i in range(1,frame_count+1):
                gen_frame_list.append(Frame(frame_list[0], bg=color ,borderwidth=borderwidth, relief=SUNKEN, width=width, height=height))
            return gen_frame_list
        
        @abstractmethod
        def child_frame_pos(self):
            pass

        def child_frame_del(self,obj_list):
            for obj in obj_list:
                obj.destroy()

        def main_frame_del(self):
            self.main_frame.destroy()

    class WinButton(ABC):
        @abstractmethod
        def button_cre(self ,f ,t ,bcl):
            pass

        def button_del(self,obj):
            obj.destroy()

    class WinLabel(ABC):
        @abstractmethod
        def label_pos(self):
            pass

        def label_del(self,obj):
            obj.destroy()

    class WinEntry(ABC):
        def entry_cre(self ,frame ,frame_count, font, hlb, hlt, color):
            entry_list=[]
            for i in range(1, frame_count+1):
                entry_list.append(Entry(frame, font = font, highlightbackground = hlb, highlightthickness = hlt, fg = color))
            return entry_list

        @abstractmethod
        def entry_pos(self):
            pass

        def entry_del(self,obj):
            obj.destroy()

        @abstractmethod
        def entry_erase(self,obj):
            pass        

    class WinRadial(ABC):
        @abstractmethod
        def radial_cre(self,frame,frame_count):
            pass

        def radial_del(self,obj_list):
            for obj in obj_list:
                obj.destroy()

    class WinMenu(ABC):
        @abstractmethod
        def menu_cre(self):
            pass

        def menu_del(self, obj):
            obj.destroy()

    class WinTextBox(ABC):
        def textbox_cre(self,frame,ht,wd):
            obj = Text(frame, height = ht, width = wd)
            return obj

        @abstractmethod
        def textbox_pos(self):
            pass

        def textbox_del(self,obj):
            obj.destroy()


class EIFace:
    class FSManager(ABC):
        def is_path_exist(self,path):
            return

        @abstractmethod
        def show_inner(self,path):
            pass

if __name__=="__main__":
    #Pop-Up Configuration
    win.mainloop()




