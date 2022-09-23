from datetime import *
from pygame import mixer
from tkinter import messagebox




class Alarm:


    def __init__(self,destination_time=None):
        self.destination_time = destination_time


    #alarm sound effect
    def set_audio_mixer(self, file_name ,volume=1):
        try:
            mixer.init()
            mixer.music.load(file_name)
            mixer.music.set_volume(volume)
        except TypeError:
            
            raise TypeError('audio file must be str and volume must be int')
        

    # set user time as time object 

    def set_user_time(self, user_time, is_stop_watch):
        if user_time:
          
            try:
                now = datetime.now()
                hours, minutes, seconds = map(int,user_time.split(':'))
                
                if is_stop_watch != 1:
                    self.destination_time = datetime(now.year, now.month, now.day,hours,minutes,seconds)
                else:
                  
                    self.destination_time = datetime(
                        now.year,
                        now.month,
                        now.day,
                        hour=now.hour+hours,
                        minute=now.minute+minutes,
                        second=now.second+seconds
                        )
                
                return 

            except ValueError:
                messagebox.showerror('Value Error', 'Invalid time \n plz enter time using HH:MM:SS format')
                raise ValueError('invalid time \n plz enter time using HH:MM:SS format')


        messagebox.showerror('Error', 'Enter something')
        raise Exception('no input')

        


    def get_current_time(self):
      
            now = datetime.now()
            now = datetime(now.year, now.month, now.day,now.hour,now.minute,now.second)
            return now
          
    
    
    def get_time_left(self, current_time):
        if current_time and self.destination_time:
            try:
               
                time_left = self.destination_time - current_time
                return time_left

            except ValueError:
                raise ValueError('plz enter a valid current time')
        
    # for the other day requests
    def add_destination_time_date(self):
        now = datetime.now()
        time_user = self.destination_time

        if time_user < self.get_current_time():
            self.destination_time = datetime(now.year, now.month, now.day+1, time_user.hour, time_user.minute, time_user.second)
               
       

        


    def play_music(self):
        mixer.music.play()


    def stop_music(self):
        
        mixer.music.stop()

    