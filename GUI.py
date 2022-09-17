from tkinter import *
from tkinter.font import Font
from PIL import Image, ImageTk




# a class for creating our Graphycal user interface
class GUI:
        def __init__(self, geometry, title):
                self.window = Tk()
                self.window.geometry(geometry)
                self.window.title(title)
                #functions
                self.run_clock_func = None
                self.stop_func = None 
                #color
                self.color = 'gray'
                #not resizable window
                self.window.resizable(False, False)
                
                self.user_time = StringVar()


        def config_font(self, family, size, weight='normal'):

                self.font1 = Font(family=family, size=size, weight=weight)

                

        def config_icon(self, iconpath):
                icon = Image.open(iconpath)
                photo = ImageTk.PhotoImage(icon)
                self.window.wm_iconphoto(False, photo)


        def set_frames(self):
                self.frame1 = Frame(self.window, highlightbackground=self.color, height='150', width='300')
                self.frame1.pack(side='top')

                self.frame2 = Frame(self.window, highlightbackground=self.color, height='50', width='300')
                self.frame2.pack(side='top')

        


        def set_buttons(self):

                self.btn_start = Button(self.frame2, text='Start', justify='center',bg='#6CD300',fg='black', width=10, command=self.run_clock_func, bd=6)
                self.btn_start.grid(column=2, row=14, pady=15, padx=5)
                
                self.btn_stop = Button(self.frame2, text='stop alarm', width=10, bg='#6CD300', fg='black', command=self.stop_func, state=DISABLED, bd=6)
                self.btn_stop.grid(column=3, row=14, pady=15, padx=5)


        def set_labels(self):
                self.lbl = Label(self.frame1, text='enter time:', fg='red', font=self.font1)
                self.lbl.grid(column=2, row=2, pady=5)
                

                self.title_lbl = Label(self.frame1, text='Alarm Clock', fg='black', font=self.font1,bd=5, bg=self.color)
                self.title_lbl.grid(column=2, row=0)


        def set_entries(self):
                self.time_input = Entry(self.frame1, width=30, textvariable=self.user_time, )
                self.time_input.grid(column=2, row=10)
                self.time_input.insert(0, 'HH:MM:SS')


        def set_time_left(self, time_left):
                left_Time = Label(self.frame1, text=f'time left : {time_left}')
                left_Time.grid(column=2,row=6, pady=10)






