import time
#Fuctions
def greet_user(name):
    print(f'Hello, {name}, Welcome to my first UI connect portal!')
    print("This is one of the first projects in Python. I" + "'" + "m just going to try a few things")

def ques(q1, name):
    print(f'{name} thanks for letting us know about {q1}')


#def book_event(event):

#input
name = input(" Hi, what is your name?")

#function call
greet_user(name)
#timer
time.sleep(5)
#input
q1 = input("What service would you like to book?")

#function call
ques(q1, name)
#input
event = input("Enter a date you like to get this done?")

#goodbye print message
print("Thanks for talking I will get this booked for you " + name + "on the "+ event +", stay safe see you again.")
