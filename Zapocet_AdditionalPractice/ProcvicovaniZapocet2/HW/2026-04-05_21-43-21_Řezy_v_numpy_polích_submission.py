import numpy as np

def search_max_sum(field: np.ndarray, size: int) -> tuple[int, np.ndarray] | None:
    """
    Najde čtverec dané velikosti s maximálním součtem prvků.
    """
    rows, cols = field.shape  # Získáme rozměry pole (řádky, sloupce)

    # 1. Kontrola, zda se čtverec do pole vůbec vejde
    if size > rows or size > cols:
        return None

    biggest_sum = -1
    best_square = None

    # 2. Procházíme všechny možné pozice levého horního rohu čtverce
    # Musíme skončit dříve, aby čtverec nevykukoval z pole ven
    for r in range(rows - size + 1):
        for c in range(cols - size + 1):
            
            # 3. Vytvoříme výřez (slice) čtverce o velikosti size x size
            # V NumPy se to dělá pomocí field[od_radku:do_radku, od_sloupce:do_sloupce]
            current_square = field[r : r + size, c : c + size]
            
            # 4. Spočítáme součet prvků v aktuálním výřezu
            current_sum = np.sum(current_square)

            # 5. Pokud je součet větší než dosavadní maximum, uložíme si ho
            # První nalezený čtverec nastavíme jako výchozí maximum
            if best_square is None or current_sum > biggest_sum:
                biggest_sum = current_sum
                best_square = current_square.copy() # .copy() pro jistotu, aby se data nezměnila

    return (biggest_sum, best_square)

def main():
    # ... zbytek tvého kódu pro main ...
    rows = 10
    cols = 15
    field_sequential = np.arange(rows * cols, dtype=int).reshape(rows, cols)
    print("Testovací pole 1 (sekvenční):")
    print(field_sequential)

    size = 3
    result = search_max_sum(field_sequential, size)
    if result:
        max_sum, square = result
        print(f"\nNejvětší součet prvků ve čtverci {size}x{size} je: {max_sum}")
        print("Čtverec:")
        print(square)
    else:
        print(f"\nDo pole se nevejde čtverec o velikosti {size}x{size}.")

    print("-" * 30)

    rows = 20
    cols = 5
    field_random = np.random.randint(100, size=(rows, cols), dtype=int)
    print("\nTestovací pole 2 (náhodné):")
    print(field_random)
    
    result_random = search_max_sum(field_random, size)
    if result_random:
        max_sum_random, square_random = result_random
        print(f"\nNejvětší součet prvků ve čtverci {size}x{size} je: {max_sum_random}")
        print("Čtec:")
        print(square_random)
    else:
        print(f"\nDo pole se nevejde čtverec o velikosti {size}x{size}.")

if __name__ == "__main__":
    main()