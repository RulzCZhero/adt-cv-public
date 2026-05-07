def passchecker(password: str) ->bool:
    specialChars = ["#", "&", "*", "!"]
    conditions=0
    if len(password)>=8 and len(password)<=16:
        conditions+=1
    for n in password:
        if n.isnumeric() and conditions<2:
            conditions+=1
    for m in password:
        if m.isupper() and conditions<3:
            conditions+=1
    for char in specialChars:
        if char in password and conditions<4:
            conditions+=1
    if conditions==4 and "123" not in password.lower() and "password" not in password.lower():
        return True
    return False

def main():
    password = input("Zadejte heslo na kontrolu: ")
    print(f"Je heslo {password} validní?: {passchecker(password)}")
    

if __name__=='__main__':
    main()