import random

#def means define
def main():
    
    #program chooses a random number to countdown from
    number = random.randint(5, 15)
    countdown(number)
    print("Happy New Year!")

def countdown(n):
    for i in range(n):
        print(n - i)

main()
#this runs the code