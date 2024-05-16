import time 
from playsound import playsound 
  
playsound("bg.mp3")  
 
def countdown(t): 
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
      
    print('Time\'s Up!') 
# input time in seconds 
t = input("Enter the time in seconds: ") 
  
# function call 
countdown(int(t)) 
