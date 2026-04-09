import os

def vytvor_mapu_produktu(cesta_k_souboru: str) -> dict:
    """
    Přečte soubor, kde každý řádek vypadá např. takto:
    Karel: chleba, máslo, jablka
    Eva: máslo, víno, sýr
    Karel: pivo, sýr
    
    Úkol: 
    Vytvoř slovník, kde klíčem bude název produktu (očištěný od mezer, malými písmeny)
    a hodnotou bude množina (set) jmen zákazníků, kteří si daný produkt někdy koupili.
    
    Poznámka: Jeden zákazník může být na více řádcích (měl více nákupů). 
    Díky použití množiny tam jeho jméno u daného produktu bude jen jednou.
    
    Očekávaný výstup pro ukázku výše:
    {
        "chleba": {"Karel"},
        "máslo": {"Karel", "Eva"},
        "jablka": {"Karel"},
        "víno": {"Eva"},
        "sýr": {"Eva", "Karel"},
        "pivo": {"Karel"}
    }
    """
    seznam = {}
    tempset = set()
    with open(cesta_k_souboru,"r",encoding="utf-8") as f:
        for lines in f:
            line = lines.strip().split(" ")
            for word in line:
                if word == line[0]:
                    name = word.replace(":","")
                else:
                    word=word.replace(",","")
                if word != line[0] and word not in seznam:
                    seznam[word] = set()
                if word != line[0]:
                    seznam[word].add(name)
    return seznam


def spolecni_zakaznici(mapa_produktu: dict, produkt1: str, produkt2: str) -> set:
    """
    Přijme slovník vytvořený předchozí funkcí a názvy dvou produktů.
    Vrátí množinu zákazníků, kteří si koupili OBA dva produkty.
    
    Nápověda: Pokud produkty ve slovníku neexistují, vrať prázdnou množinu.
    Jinak využij množinové operace (průnik).
    """
    bothProducts = set()
    oneProduct = []
    for key,value in mapa_produktu.items():
        tempvalue = list(value)
        if key == produkt1 or key == produkt2:
             for person in tempvalue:
                if person in oneProduct:
                 bothProducts.add(person)
                else:
                 oneProduct.append(person)
    return bothProducts


def main():
    data_path = os.path.join("data.txt")
    slovnik = vytvor_mapu_produktu(data_path)
    print(slovnik)
    setusmetus = spolecni_zakaznici(slovnik,"sýr","máslo")
    print(setusmetus)

if __name__ == '__main__':
    main()