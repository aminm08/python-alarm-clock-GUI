from datetime import *
from pygame import mixer
from GUI import GUI

class Alarm:
    def __init__(self,destination_time=None):
        self.destination_time = destination_time

        
    def set_audio_mixer(self, file_name ,volume=1):
        try:
            mixer.init()
            mixer.music.load(file_name)
            mixer.music.set_volume(volume)
        except TypeError:
            raise TypeError('audio file must be str and volume must be int')
        


    def set_user_time(self, user_time):

        try:
            hours, minutes, seconds = map(int,user_time.split(':'))
            self.destination_time = time(hours, minutes, seconds)

        except ValueError:
            raise ValueError('invalid datetime')
        


    def get_current_time(self):
      
            now = datetime.now()
            current_time = time(now.hour, now.minute, now.second)
            return current_time
          
    
    def get_time_left(self, current_time):
        time_left = datetime.combine(
            date.today(), self.destination_time) - datetime.combine(date.today(), current_time)

        return time_left



    def play_music(self):
        mixer.music.play()


    def stop_music(self):
        
        mixer.music.stop()

    