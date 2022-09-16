from datetime import *
from pygame import mixer


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
        


    def get_user_time(self):

        try:
            hours, minutes, seconds = map(int,input('enter a time (HH:MM:SS) :\n').split(':'))
            self.destination_time = time(hours, minutes, seconds)

        except ValueError:
            raise ValueError('invalid datetime')
        


    def run_alarm_clock(self):
        while True:
            now = datetime.now()
            current_time = time(now.hour, now.minute, now.second)
            
            if current_time >= self.destination_time:
                break
        return True
    

    def play_music(self):
        mixer.music.play()


    def stop_music(self):
    
        mixer.music.stop()

    