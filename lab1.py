
# Add book
def add(database, bookInfo):
    with open(database, 'a') as file:
        file.write('|'.join(bookInfo) + "\n")
    print("Book added successfully.")

# Remove Book
def rm(database, bookName):
    with open(database, 'r') as file:
        lines = file.readlines()
    with open(database, 'w') as file:
        for line in lines:
            if bookName not in line:
                file.write(line)
    print("Book removed successfully.")

# Modify book
def modify(database, oldInfo=None, newInfo=None):
    if not any(oldInfo):
        print("Please enter at least one old book feature.")
        return
    
    with open(database, 'r') as file:
        lines = file.readlines()

    modified = False
    with open(database, 'w') as file:
        for line in lines:
            bookInfo = line.strip().split("|")
            matching = True
            for old, new in zip(oldInfo, newInfo):
                if old and old != bookInfo[0] and old != bookInfo[1] and old != bookInfo[2] and old != bookInfo[3]:
                    matching = False
                    break
                elif old and old == bookInfo[0]:
                    modified = True
                    line = "|".join(newInfo) + "\n"
                    break
            if matching and modified:
                file.write(line)
                print("Book modified successfully.")
            else:
                file.write(line)

# Search book
def search(database, query):
    found = False
    with open(database, 'r') as file:
        for line in file:
            if query in line:
                print(line.strip())
                found = True
    if not found:
        print("No matching books found.")

# Basis of the code
def main():
    database = "library.txt"
    while True:
        mode = input("Witam w Lublin Virtual Library, enter a command (add, modify, search, rm or q to quit): ").lower()
        if mode == "q":
            break
        elif mode == 'add':
            name = input('Enter book name: ')
            author = input('Enter author name: ')
            year = input('Enter published year: ')
            genre = input('Enter genre: ')
            bookInfo = [name, author, year, genre]
            add(database, bookInfo)
        elif mode == 'search':
            query = input('Enter search query: ')
            search(database, query)
        elif mode == 'rm':
            name = input('Enter book name to remove: ')
            rm(database, name)
        elif mode == 'modify':
            oldName = input('Enter old book name (leave blank to skip): ')
            oldAuthor = input('Enter old author name (leave blank to skip): ')
            oldYear = input('Enter old published year (leave blank to skip): ')
            oldGenre = input('Enter old genre (leave blank to skip): ')
            oldInfo = [oldName, oldAuthor, oldYear, oldGenre]

            newName = input('Enter new book name: ')
            newAuthor = input('Enter new author name: ')
            newYear = input('Enter new published year: ')
            newGenre = input('Enter new genre: ')
            newInfo = [newName, newAuthor, newYear, newGenre]

            modify(database, oldInfo, newInfo)
        else:
            print('Invalid mode. Please try again.')

if __name__ == "__main__":
    main()
