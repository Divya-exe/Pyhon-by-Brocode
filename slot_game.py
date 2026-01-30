import random
def spin_row():
    symbols=['🍒','🍋','🍉','😂','🙌']
    return[random.choice(symbols) for _ in range(3)]
    
def print_row(row):
    print("********************")
    print(" | ".join(row))
    print("********************")
    
def get_payout(row ,bet):
    if row[0]==row[1]==row[2]:
        if row[0]=="🍒":
            return bet * 3
        elif row[0]=="🍋":
            return bet * 4
        elif row[0]=="🍉":
            return bet * 5
        elif row[0]=="😂":
            return bet * 10
        elif row[0]=="🙌":
            return bet * 20
    return 0    
def main():
    balance = 100
    print("********************")
    print("Welcome to slot game python")
    print("symbols: 🍒 🍋 🍉 😂 🙌")
    print("********************")
    
    while balance > 0:
        print(f"current balance is ${balance}")
        bet= input("place your bet: ")
        
        if not bet.isdigit():
            print("enter a valid amount..")
            continue
        
        bet=int(bet)
        
        if bet > balance:
            print("insufficient Funds")
            continue
            
        if bet < 0:
            print("bet must be grater then zero")
            continue
        
        balance -= bet
        
        if balance == 0:
            print("you are out of funds")
            break
        
        row = spin_row()
        print("spinning...\n")
        print_row(row)
        
        payout= get_payout(row ,bet)
        
        if payout > 0:
            print(f"you win ${payout}")
        else:
            print("sorry you lost this round")
        
        balance += payout
        
        play_again= input("do you want to play again(Y/N): ").upper()
        if play_again != "Y":
            break
    print("***********************")
    print(f"Game Over! your final balance is {balance}")
    print("***********************")
    
if __name__ == '__main__':
    main()