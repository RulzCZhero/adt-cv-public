def getStats(books:list[dict]) -> dict:
    popular = []
    programmingAuthors = set()
    bookStatus= {
        "available": 0,
        "borrowed" :0
    }
    toPurge = []
    for book in books:
        #check1
        if book["borrows"] > 100:
            popular.append(book["title"])
        #check2
        if "programming" in book["tags"]:
            programmingAuthors.add(book["author"])
        #check3
        if book["status"] == "borrowed":
            bookStatus["borrowed"]+=1
        else:
            bookStatus["available"]+=1
        #check4
        if book["borrows"] < 10 and book["status"]=="available":
            toPurge.append(book["title"])
    stats = {
        "popular_titles": popular,
        "programming_authors": list(programmingAuthors),
        "counts": bookStatus,
        "purge_list": toPurge
    }
    return stats

def main():
    library_books = [
    {"title": "Python Basics", "author": "Guido", "status": "available", "borrows": 50, "tags": ["programming", "tech"]},
    {"title": "C++ Pro", "author": "Bjarne", "status": "borrowed", "borrows": 120, "tags": ["programming", "hard"]},
    {"title": "The Hobbit", "author": "Tolkien", "status": "available", "borrows": 300, "tags": ["fantasy", "classic"]},
    {"title": "Modern AI", "author": "Altman", "status": "borrowed", "borrows": 10, "tags": ["tech", "AI"]},
    {"title": "Old Java", "author": "Unknown", "status": "available", "borrows": 5, "tags": ["programming", "old"]},
    {"title": "Harry Potter", "author": "Rowling", "status": "available", "borrows": 500, "tags": ["fantasy", "classic"]}
]
    print(getStats(library_books))
    

if __name__ == '__main__':
    main()