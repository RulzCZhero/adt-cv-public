def get_variations(length: int) -> list[str]:
    """
    Generuje variace hesel na základě zadaných kritérií.

    František zapomněl své heslo. Pamatuje si, že:
      a) obsahovalo pouze písmena k,o,p,e,s,l,i,d,r.
      b) obsahovalo písmena "lid" za sebou.
    
    Písmena se mohou v hesle opakovat.

    Tato funkce vygeneruje všechna možná hesla splňující obě podmínky (a, b) zadané délky.
    """
    # TODO implementujte logiku pro generování variací.
    # Doporučuje se pouzit pomocnou rekurzivní funkci.
    password = []
    temp = generate_string_variations("kopeslidr",length)
    for heslo in temp:
        if "lid" in heslo:
            password.append(heslo)
    return password

def generate_string_variations(alphabet: str, length: int, prefix: str = "") -> list[str]:
    """
    Rekurzivně generuje a vrací seznam řetězcových variací zadané délky z dané abecedy.
    """
    all_variations = []
    if (len(prefix) == length) and (prefix not in all_variations):
        all_variations.append(prefix)
    return all_variations

if __name__ == "__main__":
    length = 5
    print(f"Generuji hesla délky {length}.")
    variations = get_variations(length)
    print(f"Nalezeno {len(variations)} variací.")
