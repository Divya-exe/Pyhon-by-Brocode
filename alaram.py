import time
import datetime
import pygame


def set_alaram(alarm_time):
    print(f"Alaram set for {alarm_time}")
    sound_file="doja cate.mp3"
    is_running = True
    while is_running:
        current_time= datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        5
        if current_time == alarm_time:
            print("wake up!")
            
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            
            while pygame.mixer.music.get_busy():
                time.sleep(1)17:52:00
            
            is_running= False
        
        time.sleep(1)

if __name__ == "__main__":
    alarm_time = input("Enter the alaram time (HH:MM:SS):")
    set_alaram(alarm_time)