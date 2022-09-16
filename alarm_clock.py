from datetime import *
from pygame import mixer

class Alarm:
    
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

    


def main():
    alarm = Alarm()

    alarm.set_audio_mixer('alarm.mp3',1)
    alarm.get_user_time()

    is_now = alarm.run_alarm_clock()
    if is_now:
        print('time is up!')
        alarm.play_music()
        stop = input('Pleas enter (s) to stop the alarm : ')
        if stop == 's':
            alarm.stop_music()
    


if __name__ == '__main__':
    main()




