from ctypes import resize
from tkinter import *
from turtle import heading
from PIL import Image, ImageTk


class GUI:
        def __init__(self, geometry, title):
                self.window = Tk()
                self.window.geometry(geometry)
                self.window.title(title)
                self.function = None
                self.stop_func = None
                self.color = 'gray'
                self.window.resizable(False, False)
                
                self.time = StringVar()


        def config_icon(self, iconpath):
                ico = Image.open(iconpath)
                photo = ImageTk.PhotoImage(ico)
                self.window.wm_iconphoto(False, photo)

        def set_frames(self):
                self.inp1 = Frame(self.window, highlightbackground=self.color, height='100', width='300')
                self.inp1.pack(side='top')

        


        def set_buttons(self):

                self.bt = Button(self.inp1, text='set', justify='center', width=20, bg='green', command=self.function)
                self.bt.grid(column=2, row=10, pady=20)
                
                self.bt_stop = Button(self.inp1, text='stop alarm', width=20, command=self.stop_func, state=DISABLED)
                self.bt_stop.grid(column=2, row=20, pady=10)
        def set_labels(self):
                lbl = Label(self.inp1, text='enter time', bg=self.color)
                lbl.grid(column=2, row=2, pady=5)


        def set_entries(self):
                self.inp = Entry(self.inp1, width=30, textvariable=self.time)
                self.inp.grid(column=2, row=8)


        def set_error(self, text):
                lbl_eror = Label(self.inp1, text='enter time', bg=self.color)
                lbl_eror.grid(column=2, row=4, pady=5)


        def set_time_left(self, time_left):
                left_T = Label(self.inp1, text=f'time left : {time_left}')
                left_T.grid(column=2,row=6, pady=10)





















# class GUI:
#         def __init__(self) -> None:
#                 self.window = Tk()

# if __name__ == '__main__':
