def textConvertor(text: str) -> str:
    toConvert = list(text)
    leetChars={
        "a":"4",
        "e":"3",
        "i":"1",
        "o":"0",
        "s":"5"
    }
    for m,char in enumerate(toConvert):
            if char.lower() in leetChars:
                toConvert[m]=leetChars[char]
    convertedText = "".join(toConvert)
    return convertedText

def ConvertEasy(text: str) -> str:
     replaced = text.replace("a","4").replace("e","3").replace("i","1").replace("o","0").replace("s","5")
     return replaced


def main():
    text = input("Zadejte text na konverzi: ")
    print(f"Your converted text: {textConvertor(text)}")
    print(f"idk more: {ConvertEasy(text)}")

if __name__=='__main__':
    main()