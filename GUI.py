from tkinter import *
from tkinter import messagebox
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
                self.delete_history_func = None
                self.show_history_func = None
                self.restart_func = None
                #color
                self.color = 'gray'
                #not resizable window
                self.window.resizable(False, False)
                
                self.user_time = StringVar()
                self.from_now_choice = IntVar()


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
                self.btn_start.grid(column=2, row=14, pady=10, padx=5)

                self.btn_stop = Button(self.frame2, text='stop alarm', width=10, bg='#6CD300', fg='black', command=self.stop_func, state=DISABLED, bd=6)
                self.btn_stop.grid(column=3, row=14, pady=10, padx=5)

                self.btn_history = Button(self.frame2, text='show history', width=10, bg='#6CD300', fg='black', command=self.show_history_func, bd=6)
                self.btn_history.grid(column=2, row=15, pady=3, padx=5)

                self.btn_delete_history = Button(self.frame2, text='delete history', width=10, bg='#6CD300', fg='black', command=self.delete_history_func, bd=6)
                self.btn_delete_history.grid(column=3, row=15, pady=3, padx=5)

               

        def set_restart_btn(self):
                self.btn_restart = Button(self.frame2, text='restart', width=10, bg='#6CD300', fg='black', command=self.restart_func, bd=6)
                self.btn_restart.grid(column=2, row=15, pady=3, padx=5)

        def set_labels(self):
                self.lbl = Label(self.frame1, text='enter time:', fg='red', font=self.font1)
                self.lbl.grid(column=2, row=2, pady=5)
                

                self.title_lbl = Label(self.frame1, text='Alarm Clock', fg='black', font=self.font1,bd=5, bg=self.color)
                self.title_lbl.grid(column=2, row=0)


        def set_entries(self, db_time):
                self.time_input = Entry(self.frame1, width=30, textvariable=self.user_time, )
                self.time_input.grid(column=2, row=10)
                if db_time:
                        self.time_input.insert(0, db_time)

        def set_check_button(self):
                self.check_button = Checkbutton(self.frame1, text='from now?', variable=self.from_now_choice, onvalue=True, offvalue=False)
                self.check_button.grid(column=2, row=13)


        def set_time_left(self, time_left):
                left_Time = Label(self.frame1, text=f'time left : {time_left}')
                left_Time.grid(column=2,row=6, pady=10)

        def on_close(self):
                if messagebox.askokcancel('Quit', "do you want to quit?"):
                        self.window.destroy()

        def add_message(self, title:str, message:str):
                messagebox.showinfo(title, message)




