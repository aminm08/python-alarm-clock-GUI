
from tkinter import *
from datetime import *
from alarm import Alarm
from GUI import GUI
from database import DB
from pygame.time import Clock

def run_clock():
  

    #set the destination time

    alarm.set_user_time(app.time_input.get(), app.from_now_choice.get())
    user_time = alarm.destination_time

    #add time to db
    db.add_time_to_db(str(time(user_time.hour, user_time.minute, user_time.second)))
    

    # applying changes on GUI
    app.btn_start['state'] = DISABLED
    app.time_input.delete(0, 'end')
    app.time_input.destroy()
    app.check_button.destroy()
    app.lbl.destroy()
    app.btn_history.destroy()
    app.btn_delete_history.destroy()

    
    #alarm clock
    while True:
        
        current_time = alarm.get_current_time()


        alarm.add_destination_time_date()
        time_left = alarm.get_time_left(current_time)

       
        app.set_time_left(time_left)

        app.window.update()

        if current_time == alarm.destination_time:
                break   

        # to run the loop twice/second
        clock.tick(3)
        

    
    alarm.play_music()
    app.set_restart_btn()
    app.btn_stop['state'] = 'active'
    

def show_history():
    history = db.get_all_records()
    message = ''
    
    for i in history:
        print(i)
        message += f'{i[0]}.({i[1]})\n'

    app.add_message('time history', message) if message else app.add_message('time_history', 'no history')
    



def restart():
    app.frame1.destroy()
    app.frame2.destroy()
    app.set_frames()
    app.set_buttons()
    app.set_labels()
    app.set_entries(alarm.config_user_previous(last_hour))
    app.set_check_button()




if __name__ == '__main__':
    #config GUI and alarm
    app = GUI('300x200', 'alarm Clock')
    alarm = Alarm()
    clock = Clock()
    db = DB()
    
    #database table creation
    db.create_table()

    last_hour = db.read_last_time()
   
    #config icon forn and audio
    alarm.set_audio_mixer('assets/alarm.mp3',1)
    app.config_icon('assets/logo.png')
    app.config_font('Helvetica', 10, 'bold')

    #define alarm functions
    app.run_clock_func = run_clock
    app.stop_func = alarm.stop_music
    app.delete_history_func = db.delete_all_records
    app.show_history_func = show_history
    app.restart_func = restart

    # set GUI
    app.set_frames()
    app.set_buttons()
    app.set_labels()
    app.set_entries(alarm.config_user_previous(last_hour))
    app.set_check_button()

    app.window.protocol("WM_DELETE_WINDOW", app.on_close)
    app.window.mainloop()

