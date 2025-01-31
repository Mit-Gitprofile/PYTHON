import time
from datetime import datetime

def countdown(second):

    while second>=0:        #countdown time using time.sleep(1-second)
        print(f"Time left:{second} seconds",end="\r")
        time.sleep(1)
        second-=1

    print("\nTime's up!")

def stopwatch():
    while True:
        print("Enter your choise:")
        print("1. Start")
        print("2. Stop")
        choise=int(input("Enter your choise:"))

        if choise==1:       #starting....
            start=datetime.now()
            print("Start Time:",start.strftime("[%m/%d/%Y, %H:%M:%S]"))
            print("Starting....\n")

        elif choise==2:     #Ending....
            end=datetime.now()
            print("End Time:",end.strftime("[%m/%d/%Y, %H:%M:%S]"))
            print("Ending....\n")

            result=end-start    #Diffrent calculation
            print("Diffrent Time:",result,"\n")
            break

        else:
            print("Invelid Choise...")