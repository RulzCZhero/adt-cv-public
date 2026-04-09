from pathlib import Path

def main():
    try:
        with open("data.txt","r",encoding="utf-8") as f:
            for i, n in enumerate(f):
                print(f"{i+1}: {n.strip()}") #místo enumerate jde tky prostě cislo=1 a po každym výpisu cislo+=1
    except FileNotFoundError:
        print("Soubor 'data.txt' nebyl nalezen.")


if __name__ == '__main__':
    main()