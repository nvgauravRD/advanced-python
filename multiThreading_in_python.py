import threading
from time import sleep

Process_Execute = True

# function prints odd num
def PrintOdd():
    num = 1
    while Process_Execute:
        sleep(2) # to delay for 2sec
        print("Printing odd",num)
        num += 2

# function prints even num
def PrintEven():
    num = 0
    while Process_Execute:
        sleep(2) # to delay for 2sec
        print("Printing even",num)
        num += 2

# greets user
def greet(userName):
    print(f"Hello, {userName}")

# declaring main threads
odd_thread = threading.Thread(target=PrintOdd)
even_thread = threading.Thread(target=PrintEven)

# daemon thread stops if main threads stops excuting
# set daemon=True
# args of function should be passed as tuple ( can be used in main thread as well)
daemon_thread = threading.Thread(target=greet, daemon=True, args=("Gaurav",))

odd_thread.start()
even_thread.start()
daemon_thread.start()

print("Press Enter to quit")
input()
Process_Execute = False

"""
Output

$ py multiThreading_in_python.py 
Hello, Gaurav
Press Enter to quit
Printing even 0
Printing odd 1
Printing odd 3
Printing even 2

Printing odd 5
Printing even 4
"""
