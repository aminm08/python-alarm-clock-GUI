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
    #you can implement this method if you don't need GUI 
    def set_user_time(self, user_time, is_stop_watch):
        if user_time:
          
            try:
                now = datetime.now()
                hours, minutes, seconds = map(int,user_time.split(':'))
                
                if is_stop_watch != 1:
                    self.destination_time = time(hours,minutes,seconds)
                else:
                  
                    self.destination_time = time(
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
            current_time = time(now.hour, now.minute, now.second)
            return current_time
          
    
    
    def get_time_left(self, current_time):
        if current_time and self.destination_time:
            try:
                time_left = datetime.combine(
                    date.today(), self.destination_time) - datetime.combine(date.today(), current_time)
                return time_left

            except ValueError:
                raise ValueError('plz enter a valid current time')
        

        



    def play_music(self):
        mixer.music.play()


    def stop_music(self):
        
        mixer.music.stop()

    