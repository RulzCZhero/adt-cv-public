def gcd(a: int, b: int) -> int:
    if(a==b):
        return a
    if(a<b):
        mensi = a
        vetsi = b
    else:
        mensi = b
        vetsi = a
    if(mensi<0):
        mensi=-mensi
    if(vetsi<0):
        vetsi=-vetsi
    
    if(a == 0 or b == 0):
        if vetsi<0:
            return-mensi
        else:
            return mensi
    if (vetsi%mensi==0):
        return mensi
    return gcd(vetsi%mensi,mensi)

def nsn(a: int, b: int, candidate: int = None) -> int:
    a, b = abs(a), abs(b)
    if a == 0 or b == 0:
        return 0
    
    vetsi = max(a, b)
    mensi = min(a, b)
    
    if candidate is None:
        candidate = vetsi

    if candidate % mensi == 0:
        return candidate
    
    return nsn(mensi, vetsi, candidate + vetsi)

    #daily interest: account.balance = account.balance*(1+(accoun.daily_interest_rate/100))

def main():
    print(gcd(345,766))
    print(nsn(976,84))

if __name__ == '__main__':
    main()