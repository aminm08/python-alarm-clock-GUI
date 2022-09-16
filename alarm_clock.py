from alarm import Alarm
from GUI import AppGUI
from PyQt5.QtWidgets import QApplication
import sys
from datetime import *

def main():
    
    alarm = Alarm()

    h, m, s = map(int,win.user_time.split(':'))
    dest = time(h,m,s)
    alarm.destination_time = dest
    # sys.exit(app.exec_())
    alarm.set_audio_mixer('alarm.mp3',1)
    # alarm.get_user_time()
    is_now = alarm.run_alarm_clock()
    if is_now:
        print('time is up!')
        alarm.play_music()
        stop = input('Pleas enter (s) to stop the alarm : ')
        if stop == 's':
            alarm.stop_music()
    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = AppGUI()
    win.show()
    app.exec()
    if win.user_time is not None:
        app.exit()
        win.close()
        main()
    





