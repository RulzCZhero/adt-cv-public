# Testovací data: Jméno čtenáře, ID čtenáře, ISBN, Pobočka
# Takto mohou vypadat záznamy načtené z CSV nebo databáze.
raw_data: list[tuple[str, str, str, str]] = [
    ("Anna Malá",       "R-0001", "9788087222546", "Centrum"),
    ("Bohuslav Hruška", "R-0002", "9788027100002", "Centrum"),
    ("Anna Malá",       "R-0001", "9788027100003", "Sever"  ),
    ("Cyril Veselý",    "R-0003", "9788025700303", "Jih"    ),
    ("Dana Krátká",     "R-0004", "9788027100005", "Sever"  ),
    ("Annn Maláááá",    "R-0001", "9788087222546", "Centrum"),
    ("Hana Blažková",   "R-0009", "9788027100010", "Západ"  ),
    ("Ivan Král",       "R-0010", "9788027100011", "Západ"  ),
    ("ivan kakrál",     "R-0010", "9788027100011", "Západ"  ),
    ("Anna Malá",       "R-0001", "9788027100012", "Centrum"),
    ("Dana Krátká",     "R-0004", "9788027100013", "Sever"  ),
    ("Jitka Jelínková", "R-0011", "9788027100014", "Východ" ),
    ("~█r-█ ?e###o",    "R-0003", "9788025700303", "Jih"    ),
    ("██r██ █e█e██",    "R-0003", "9788025700303", "Jih"    ),
    ("Anna Malá",       "R-0001", "9788087222546", "Jih"    ), # pozor, toto není duplicitní!
]

def find_duplicate_entries(data: list[tuple[str, str, str, str]]) -> list[tuple[str, str, str, str]]:
    """
    Nalezne a vrátí duplicitní záznamy v datech.

    Duplicitní záznamy mají shodné (reader_id, isbn, branch):
      duplicitní: ("R-0001", "9788087222546", "Centrum") == ("R-0001", "9788087222546", "Centrum")
    ale:
      neduplicitní: ("R-0002", "9788087222546", "Centrum") != ("R-0001", "9788087222546", "Centrum")

    Funkce vrací opakované výskyty záznamů k odebrání.
    Pokud jsou např. 3 opakované hodnoty, tak funkce vrátí druhé dva výskyty dané výpůjčky.
    """
    duplicates: list[tuple[str, str, str, str]] = []
    
    seen_keys = set()

    for record in data:
        
        name , id_reader, isbn, branch = record
        
        key = (id_reader, isbn, branch)
        
        if key in seen_keys:
            duplicates.append(record)
        else:
            seen_keys.add(key)

    return duplicates

def main() -> None:
    # funkci main si můžete uzpůsobit jak chcete,
    # slouží pouze pro vyzkoušení programu, nikoliv hodnocení
    duplicates = find_duplicate_entries(raw_data)

    print(f"Removing {len(duplicates)} duplicates (expected 4)...")
    for dup in duplicates:
        raw_data.remove(dup)
        print(f"- {dup} successfully removed!")

    duplicates2 = find_duplicate_entries(raw_data)
    print(f"Duplicates left after deduplication {len(duplicates2)}. (Should be 0.)")


if __name__ == "__main__":
    main()
