import random as r

colors = ["red", "orange", "yellow","green","blue","violet"]

def deposit():
    while True:
        deposit = input("Enter amount to deposit $")
        if deposit.isdigit():
            deposit = int(deposit)
            if deposit > 0:
                break
            else:
                print("\nEnter a valid amount.")
        else:
            print("\nEnter a valid number.")
    return deposit

def bet():
    while True:
        bet = input("Enter a bet $")
        if bet.isdigit():
            bet = int(bet)
            if bet > 0:
                break
            else:
                print("\nEnter a valid amount.")
        else:
            print("\nEnter a valid number.")
    return bet

def spin():
    results = []
    for i in range(3):
        roll = r.randint(0, 5)
        results.append(colors[roll])
    return results




def color_game(balance, results):
    while True:
        betting = bet()   
        if betting > balance:
            print(f"You don't have enough that much money, your balance is only ${balance} ")
        else:
            break
    
    print("red  | orange | yellow |") 
    print("blue | green  | violet |")   
    while True:    
        color = input("Choose your betting color: ")
        if color.isalpha():
            if color.lower() not in colors:
                print("\nPlease enter valid betting color.")
            else:
                if color.lower() in results:
                    if len(results) != len(set(results)):
                        sets = set(results)
                        if len(sets) == 2:
                            print(f"[{', '.join(results)}]")
                            print(f"You won twice")
                            return betting * 3
                        else:
                            print(f"[{', '.join(results)}]")
                            print(f"You won thrice")
                            return betting * 4
                    else:
                        print(f"[{', '.join(results)}]")
                        print("You won once")
                        return betting * 2
                else:
                    print(f"[{', '.join(results)}]")
                    print(f"You lost")
                    return -betting 
        else:
            print("Please choose a betting color.")

def main():
    balance = deposit()
    results = spin()
    while True:
        print(f"Current balance is ${balance}")
        flag = input("\nEnter to play (type q to quit): ")
        if flag.lower() == "q":
            break
        else:
            balance += color_game(balance, results)
    

main()

