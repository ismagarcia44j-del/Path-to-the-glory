def main():
    history_num=[]
    history_sym=[]
    balance = 0
    deposit = 0
    withdraw = 0
    
    while True:
        try: 
            frcommand=input("Command: ")
            match frcommand:
                case "deposit":
                    deposit,balance,history_sym,history_num=trans_deposit(deposit,balance,history_sym,history_num)
                    print(f"Balance: ${balance:.2f}")
                case "withdraw":
                    withdraw,balance,history_sym,history_num=trans_withdraw(withdraw,balance,history_sym,history_num)
                    print(f"Balance: ${balance:.2f}")
                case "balance":
                    print(f"Balance: ${balance:.2f}")
                case "history":
                    for i in range(len(history_num)):
                        print(f"{history_sym[i]} ${history_num[i]:.2f}")
                case "quit":
                    exit()
        except (ValueError, TypeError):
            continue

def trans_deposit(deposit,balance,history_sym,history_num):
    while True:
        try:  
            new_dep=int(input("Amount: "))
            deposit=deposit+new_dep
            balance=balance+new_dep
            history_sym.append("+")
            history_num.append(new_dep)
            return deposit,balance,history_sym,history_num
        except (ValueError, TypeError):
            continue

def trans_withdraw(withdraw,balance,history_sym,history_num):
    while True:
        try:
            new_wit=int(input("Amount: "))
            if new_wit<=balance:
                withdraw=withdraw-new_wit
                balance=balance-new_wit
                history_sym.append("-")
                history_num.append(new_wit)
                return withdraw,balance,history_sym,history_num
            else:
                print("Not enough funds")
                break
        except (ValueError, TypeError):
            continue
main()
