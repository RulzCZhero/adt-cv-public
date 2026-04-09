def vytvor_invertovany_index(cesta_k_souboru: str) -> dict:
    """
    Přečte textový soubor. Každý řádek v souboru představuje jeden "dokument".
    Řádky si čísluj od 1 (první řádek má index 1, druhý 2, atd.).
    
    Úkol: Vytvoř "invertovaný index" – slovník, kde:
    - Klíčem je unikátní slovo (převedené na malá písmena).
    - Hodnotou je množina (set) čísel řádků, na kterých se slovo vyskytuje.
    
    Příklad vstupu v souboru:
    Pes štěká.
    Kočka mňouká a pes spí.
    
    Očekávaný výstup:
    {
        "pes": {1, 2},
        "štěká": {1},
        "kočka": {2},
        "mňouká": {2},
        "a": {2},
        "spí": {2}
    }
    
    Nápověda: Nezapomeň slova očistit od základní interpunkce (tečky, čárky),
    aby se "štěká." a "štěká" nebraly jako dvě různá slova. Pro číslování
    řádků se ti může hodit vestavěná funkce `enumerate()`.
    """
    words = {}
    with open(cesta_k_souboru,"r", encoding="utf-8") as f:
        for i,lines in enumerate(f,1):
            line=lines.strip().lower().split(" ")
            for word in line:
                if word.lower() not in words:
                    words[word] = set()
                words[word].add(i)
    return words

            

def main():
    slovnik = vytvor_invertovany_index("data.txt")
    print(slovnik)

if __name__ == '__main__':
    main()