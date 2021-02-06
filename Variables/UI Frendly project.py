import time
def greet_user(name):
    print(f'Hello, {name}, Welcome to my first UI connect portal!')
    print("This is one of the first projects in Python. I" + "'" + "m just going to try a few things")



name = input(" Hi, what is your name?")
greet_user(name)
time.sleep(5)
q1 = input("How can I help you today?")

print("Thanks for talking " + name + " Stay safe!")