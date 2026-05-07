# 0 = volno, 1 = zeď
bludiste = [
    [0, 0, 1],
    [1, 0, 0],
    [1, 1, 0]
]

# Příprava prázdné mapy pro výsledek
mapa = [
    [".", ".", "."],
    [".", ".", "."],
    [".", ".", "."]
]

def vyres(r, s):
    # 1. KONTROLA: Jsem mimo mapu nebo na zdi?
    if r < 0 or r > 2 or s < 0 or s > 2 or bludiste[r][s] == 1:
        return False
    
    # 2. KONTROLA: Už jsem tu značku položil? (abych se netočil v kruhu)
    if mapa[r][s] == "X":
        return False

    # 3. Akce: Položím značku
    mapa[r][s] = "X"
    print(f"Zkouším políčko [{r}, {s}]")

    # 4. CÍL: Jsem v pravém dolním rohu?
    if r == 2 and s == 2:
        print("MÁM TO! Našel jsem cestu ven.")
        return True

    # 5. REKURZE: Zkusím jít všemi směry
    # Zkusím DOLŮ, pak DOPRAVA, pak NAHORU, pak DOLEVA
    if vyres(r + 1, s) or vyres(r, s + 1) or vyres(r - 1, s) or vyres(r, s - 1):
        return True

    # 6. BACKTRACKING: Pokud ani jeden směr nevyšel, tudy cesta nevede.
    # Seberu značku a nahlásím chybu.
    print(f"Slepá ulička na [{r}, {s}], vracím se a mažu značku.")
    mapa[r][s] = "."
    return False

# SPUŠTĚNÍ
print("STARTUJEME HLEDÁNÍ:")
if vyres(0, 0):
    print("\nKonečná cesta:")
    for radek in mapa:
        print(" ".join(radek))
else:
    print("\nCesta neexistuje.")