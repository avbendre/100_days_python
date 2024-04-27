import random
def guess(x):
    rand = random.randint(1,x)
    guess = 0
    while guess!=rand:
        guess = int(input(f"guess the random number by the computer between 1 and {x} \n"))
        if guess<rand:
            print("the rand is higher than the number")
        elif guess>rand:
            print("the rand is lower than the number")
    print("You found the correct number!")

guess(10)