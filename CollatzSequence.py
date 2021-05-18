global ans


def collatz(number):
    global ans
    if number % 2 == 0:
        ans = number//2
    else:
        ans = 3 * number + 1


try:
    collatz(int(input("Enter number:")))
    while True:
        print(ans)
        if ans == 1:
            break
        collatz(ans)
        
except ValueError:
    print("Please enter an INTEGER!")
