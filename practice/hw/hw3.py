def parse_personal_data(data_string: str) -> tuple[str, str, int, int, int] | None:
    """
    Parses a string containing personal data in the format "name;surname;day.month.year".

    Args:
        data_string: The string to parse.

    Returns:
        A tuple (name, surname, day, month, year) with integer date parts,
        or None if the format is invalid.
    """
    # Implementujte logiku pro rozdělení řetězce, převod částí data na celá čísla,
    # a extrakci dat.
    # Pokud je formát nesprávný nebo převod selže, vraťte None.
    listus = data_string.split(";")
    cislus = 2
    if len(listus) == 3:
        templistus =listus[2].split(".")
        if len(templistus)==3:
            for n in templistus:
                if cislus<len(listus) and n.isnumeric():
                    listus[cislus]=int(n)
                    cislus+=1
                elif n.isnumeric():
                    listus.append(int(n))
                    cislus+=1
        if len(listus) == 5:
            return(tuple(listus))
        else:
            return None
    else:
        return None

# Vstupní bod pro demonstraci funkčnosti
if __name__ == "__main__":
    print(parse_personal_data("Jan;Novák;24.12.2020"))
    print(parse_personal_data("Peter;Pan;01.01.1990"))
    print(parse_personal_data("Neplatný;vstup"))
    print(parse_personal_data("Jan;Novák;24-12-2020"))
    print(parse_personal_data("Jan;Novák;den.mesic.rok"))
