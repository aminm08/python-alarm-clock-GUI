from alarm import Alarm
from tkinter import *
from PIL import Image, ImageTk
from GUI import GUI
from datetime import *

def run_clock():
  

    alarm.set_user_time(app.inp.get())
    if ValueError:
        app.set_error('invalid time')

    app.bt['state'] = DISABLED
    app.bt_stop['state'] = 'active'
    app.inp.delete(0, 'end')
    
    while True:
        
        current_time = alarm.get_current_time()
        time_left = alarm.get_time_left(current_time)

        app.set_time_left(time_left)

        app.window.update()
        if current_time >= alarm.destination_time:
                break   
        

    
    alarm.play_music()
    





if __name__ == '__main__':
    
    app = GUI('300x200', 'alarm Clock')
    alarm = Alarm()
    alarm.set_audio_mixer('alarm.mp3',1)

    app.config_icon('logo.png')

    app.function = run_clock
    app.stop_func = alarm.stop_music
    app.set_frames()
    app.set_buttons()
    app.set_labels()
    app.set_entries()



    app.window.mainloop()
