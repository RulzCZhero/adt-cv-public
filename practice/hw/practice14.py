import os
import sys

def get_file_content(root:str, city:str, day:str, shop:str) ->list[str]:
    data_path = os.path.join(root,city,day,shop)
    ID_list = set()
    try:
     with open(data_path,"r",encoding="utf-8") as f:
        f.readline()
        for lines in f:
            line = lines.strip().split(";")
            ID_list.add(line[2])
    except FileNotFoundError:
        print("Error! File not found!")
        sys.exit(1)
    return list(ID_list)

def kdo_ceka_na_maso(data):
    return data["meat_q"]-data["meat_X"]


def main():
    data = {"gate": {1, 2, 3}, "meat_q": {1, 2}, "meat_X": {1}}
    if len(sys.argv) >= 5:
        root = sys.argv[1]
        city = sys.argv[2]
        day = sys.argv[3]
        shop = sys.argv[4]
    else:
        print("Missing arguments!")
        print("Usage: python practice14.py <root_directory_for_data> <city> <day> <shop>")
        sys.exit(1)
    if not os.path.isdir(root):
        print(f"{root} is not a directory!")
        sys.exit(1)
    content = get_file_content(root,city,day,shop)
    for n in content:
        print(n)
    print(f"{kdo_ceka_na_maso(data)} stále čeká na maso.")
    


if __name__ == '__main__':
    main()