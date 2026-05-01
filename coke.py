#Week 2, problem set 0, Que 2. 
#A Machine sells bottles of Coca-Cola for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents, and 1 cent. Write a program that takes as input the amount of money (in cents) that a customer has inserted into the machine, and outputs the change (in cents) that the machine should return to the customer.
print("Amount due: 50")

def machine():
    total = 50
    p = 0
    while p == 0:
        user_input = int(input("Insert Coin: "))
        if user_input != 25 and user_input != 10 and user_input != 5:
            print("Amount due: 50")
            continue
        else:
            due = total - user_input
            if due > 0:
                print("Amount due: " + str(due))
                total = due
                continue
            elif due < 0:
                print("Change Owed: " + str(-due))
                p=1
                break
            else:
                print("Change Owed: 0")
                p=1
                break

machine()
