
def getInventory(delivery:list[str])-> dict[str,int]:
    inventory = {}
    for n in delivery:
        if n not in inventory:
            inventory[n]=1
        else:
            inventory[n]+=1
    return inventory

def checkAmount(inventory:dict[str,int]) -> None:
    for n in inventory:
        if inventory[n]<2:
            print(f"Warning: Low stock on {n} ({inventory[n]})")

def main():
    delivery = ["Smažák", "Polévka", "Smažák", "Kofola", "Polévka", "Smažák", "Pivo"]
    inventory = getInventory(delivery)
    print(f"Current inventory: {inventory}")
    checkAmount(inventory)
if __name__ == '__main__':
    main()