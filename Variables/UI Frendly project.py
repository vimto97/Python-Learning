import time
def greet_user(name):
    print(f'Hello, {name}, Welcome to my first UI connect portal!')
    print("This is one of the first projects in Python. I" + "'" + "m just going to try a few things")

def ques(q1, name):
    print(f'{name} thanks for letting us know about {q1}')


def book_event(event):


name = input(" Hi, what is your name?")
greet_user(name)
time.sleep(5)
q1 = input("What service would you like to book?")


ques(q1, name)
event = input("Enter a date you like to get this done?")

time.sleep(5)
print("Thanks for talking I will get this booked for you " + name + "On the "+ event +" stay safe see you again.")
