def is_safe(row: list[str]) -> bool:
    temp = ""
    for n in row:
        if temp == n:
            return False
        temp = n
    return True
        

def main():
    seatingList = ["BIO", "KIV", "KIV", "MAT"]
    print(is_safe(seatingList))

    
if __name__ == '__main__':
    main()