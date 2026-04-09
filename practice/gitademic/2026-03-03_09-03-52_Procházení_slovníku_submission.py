def print_stock_items(stock: dict[str, int]) -> None:
    """
    Iterates through a dictionary using .items() and prints each product and its quantity.
    """
    # Použijte cyklus for a metodu .items() pro získání klíče i hodnoty každé položky ve slovníku.
    # Vypište je ve formátu: 'Produkt: {key}, Množství: {value}'
    for n,m in stock.items():
        print(f"Produkt: {n}, Množství: {m}")

def print_stock_keys(stock: dict[str, int]) -> None:
    """
    Iterates through a dictionary using .keys() and prints each product name.
    """
    # Použijte cyklus for a metodu .keys() pro získání klíčů ze slovníku.
    # Vypište každý název produktu ve formátu: 'Produkt: {key}'
    for n in stock.keys():
        print(f"Produkt: {n}")
    

def main():
    """
    Hlavní funkce pro demonstraci iterace slovníkem.
    """
    product_stock = {
        "Jablka": 10,
        "Hrušky": 5,
        "Banány": 20,
        "Pomeranče": 15
    }

    print("--- Výpis pomocí .items() ---")
    print_stock_items(product_stock)
    
    print("\n--- Výpis pomocí .keys() ---")
    print_stock_keys(product_stock)

main()
