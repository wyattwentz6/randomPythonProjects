import time

# created the function that count downs 
# t is the time in seconds
def countdown(t):
    #using a while loop
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Time is up!')

t = input('Enter time in seconds: ')

countdown(int(t))
