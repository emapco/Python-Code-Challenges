import time as t
import sched
import winsound as ws
from playsound import playsound


# Sets an alarm for alarm_time seconds into future
# alarm plays the sound_file and prints to console a message
def set_alarm(alarm_time, sound_file_path, message):
    alarm_on = True
    while alarm_on:
        t.sleep(1)
        if t.time() >= alarm_time:
            print(message)
            playsound(sound_file_path)
            alarm_on = False

def solution(alarm_time, wav_file, message):
    # scheduler object with time and sleep methods to control when events execute
    s = sched.scheduler(t.time, t.sleep)
    # enterabs method to schedule an event to execute at an absolute time
    # alarm_time is time at which the event is executed, 1 is the highest priority,
    # print is the function that is called when event is executed,
    # argument contains a list of arguments to pass to the print function
    s.enterabs(alarm_time, 1, print, argument=(message,))
    # calls ws.PlaySound method with arguments specified in keyword argument 'argument'
    s.enterabs(alarm_time, 1, ws.PlaySound, argument=(wav_file, ws.SND_FILENAME))
    print("Alarm set for", t.asctime(t.localtime(alarm_time)))
    s.run()


if __name__ == '__main__':
    print("My solution:")
    set_alarm(t.time() + 5, 'alarm.wav', 'Wake up!')
    print("\nInstructor solution:")
    solution(t.time() + 5, 'alarm.wav', 'Wake up!')
