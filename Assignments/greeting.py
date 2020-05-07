#write a program that prints "good morning", "goood afternoon", and "good evening" depending on the time of the day

#this is the datetime module, you can do cool time stuff with it
import datetime

#this gives you the current time
now = datetime.datetime.today()

#python uses military time; 0-24
if now.hour in range (0,12):
    print("Good morning.")
elif now.hour in range (12, 18):
    print("Good afternoon.")
elif now.hour in range (18, 24):
    print("Good night.")