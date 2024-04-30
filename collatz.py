# simple program to print the sequence of the collatz conjecture for any number given as input
import time


def collatz(num):
    count = 0

    if num < 1:
        print("Collatz sequence only takes in positive numbers")
        return count
    
    while num > 1:
        width = 5
        time.sleep(0.2)
        if num % 2 == 0:
            print(f"{str(count).rjust(width)} )  {num}")
            num /= 2
        else:
            print(f"{str(count).rjust(width)} )  {num}")
            num = (3 * num) + 1

        num = int(num)
        count += 1
    
    print(f"{str(count).rjust(width)} )  {num}")
    print(f"\nIt took {count} steps to get down to the cyclic sequence of 1 -> 2 -> 4 -> 1 ...")
    return count
    

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
    
    collatz(num)
    # print(f"\nIt took {steps} steps to get down to the cyclic sequence of 1 -> 2 -> 4 -> 1 ...")


if __name__ == "__main__":
    main()

