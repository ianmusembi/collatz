# simple program to print the sequence of the collatz conjecture for any number given as input

import time

def collatz_recursive(num):
    return collatz_recursive_helper(num,0)

def collatz_recursive_helper(num, count):
    time.sleep(0.2)
    num = int(num)
    width = 5
    print(f"{str(count).rjust(width)} )  {num}")
    if num < 1:
        print("Collatz sequence only takes in positive numbers")
    if num == 1:
        print(f"\nIt took {count} steps to get down to the cyclic sequence of 1 -> 2 -> 4 -> 1 ...")
        return count
    elif num % 2 == 0:
        return collatz_recursive_helper(num / 2, count + 1)
    else:
        return collatz_recursive_helper((num*3) + 1, count + 1)
def main():
    incorrect = True
    while incorrect:
        num = input("Enter a number to generate it's collatz conjecture sequence: ")

        if num.isnumeric():
            num = int(num)
            incorrect = False
        elif num.lower() == 'q':
            print("Exiting... Bye!!")
            return
    
    steps = collatz_recursive(num)

    print(f"\nIt took {steps} steps to get down to the cyclic sequence of 1 -> 2 -> 4 -> 1 ...")


if __name__ == "__main__":
    main()
