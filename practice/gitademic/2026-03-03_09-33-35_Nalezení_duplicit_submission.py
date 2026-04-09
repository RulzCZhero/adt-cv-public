def find_duplicates(data: list[int]) -> set[int]:
    """
    Finds duplicate elements in a list of integers.

    Args:
        data (list[int]): List of integers.

    Returns:
        set[int]: Set containing duplicate elements.
    """
    # Vytvořte dvě množiny: jednu pro sledování již viděných čísel
    # a druhou pro ukládání nalezených duplicit.
    # Projděte vstupní seznam a pro každé číslo zkontrolujte,
    # zda jste ho již viděli. Pokud ano, přidejte ho do množiny duplicit.
    # V opačném případě ho přidejte do množiny viděných čísel.
    # Na konci vraťte množinu duplicit.
    duped = set()
    baseset= set()
    for n in data:
        if n in baseset:
            duped.add(n)
        baseset.add(n)
    return(duped)    


def demonstrate_find_duplicates(test_list: list[int]):
    """
    Runs the find_duplicates function on a list and prints the result.
    """
    print(f"Původní seznam: {test_list}")
    duplicates = find_duplicates(test_list)
    print(f"Nalezené duplicity: {duplicates}")
    print("-" * 20)

def main():
    """
    Main function for demonstrating duplicate finding.
    """
    demonstrate_find_duplicates([1, 2, 3, 4, 2, 5, 6, 3])
    demonstrate_find_duplicates([10, 20, 30, 40, 50])
    demonstrate_find_duplicates([])

main()
