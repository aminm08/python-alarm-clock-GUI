from tkinter import *
from datetime import *
from alarm import Alarm
from GUI import GUI
from pygame.time import Clock

def run_clock():
  

    #set the destination time
    alarm.set_user_time(app.time_input.get())

    # applying changes on GUI
    app.btn_start['state'] = DISABLED
    app.time_input.delete(0, 'end')
    app.time_input.destroy()
    app.lbl.destroy()
    
    #alarm clock
    while True:
        
        current_time = alarm.get_current_time()
        time_left = alarm.get_time_left(current_time)

        app.set_time_left(time_left)

        app.window.update()

        if current_time >= alarm.destination_time:
                break   
        # to run the loop twice/second
        clock.tick(2)
        

    
    alarm.play_music()
    app.btn_stop['state'] = 'active'
    





if __name__ == '__main__':
    #config GUI and alarm
    app = GUI('300x200', 'alarm Clock')
    alarm = Alarm()
    clock = Clock()
    
    #config icon forn and audio
    alarm.set_audio_mixer('alarm.mp3',1)
    app.config_icon('logo.png')
    app.config_font('Helvetica', 10, 'bold')

    #define alarm functions
    app.run_clock_func = run_clock
    app.stop_func = alarm.stop_music

    # set GUI
    app.set_frames()
    app.set_buttons()
    app.set_labels()
    app.set_entries()



    app.window.mainloop()
