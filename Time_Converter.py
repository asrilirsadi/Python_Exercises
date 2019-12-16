import math

def timeConverter(seconds):
    if seconds < 360000 and seconds >= 0:
        hours = math.floor(seconds/3600)
        minutes = math.floor((seconds%3600)/60)
        seconds = math.floor((seconds%3600)%60)

        if hours >= 0 and hours < 10:
            hours = str(hours).zfill(1+len(str(hours)))
        if minutes >= 0 and minutes < 10:
            minutes = str(minutes).zfill(1+len(str(minutes)))
        if seconds >= 0 and seconds < 10:
            seconds = str(seconds).zfill(1+len(str(seconds)))

        print('{}:{}:{}'.format(hours, minutes, seconds))
    else:
        print('invalid input')

timeConverter(3600)
timeConverter(7201)
timeConverter(359999)
