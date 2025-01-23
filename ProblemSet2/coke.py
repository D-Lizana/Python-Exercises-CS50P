# In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, 
# each time informing the user of the amount due. Once the user has inputted at least 50 cents, 
# output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.

coke = 50
coins = [5,10,25]

while coke > 0:
    inserted_coin = int(input("Insert Coin: "))
    if inserted_coin in coins:
        coke = coke - inserted_coin
        if coke > 0:
            print(f"Amount Due: {coke}")
        else:
           print(f"Change Owed: {coke*-1}")
    


