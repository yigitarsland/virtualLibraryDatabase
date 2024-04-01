
# Add book
def add(database, bookInfo):
    with open(database, 'a') as file:
        file.write(str(bookInfo) + '\n')
    print("Book added successfully.")

# Remove Book
def rm(database, name):
    with open(database, 'r') as file:
        lines = file.readlines()
    with open(database, 'a') as file:
        for line in lines:
            if name in line:
                del line
                file.write(lines)
    print("Book removed successfully.")

# Modify book
def modify(database, oldInfo=None, newInfo=None):
    with open(database, 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        features = [element.strip("' ") for element in line.strip().strip("[]").split(",")]
        if any(oldElement in features for oldElement in oldInfo):
            modifiedIndices = [idx for idx, element in enumerate(features) if element in oldInfo]
            for idx in modifiedIndices:
                features[idx] = newInfo[idx]
            lines[i] = str(features) + '\n'
            with open(database, 'w') as file:
                file.writelines(lines)
            print('Book modified successfully.')
            break # Exit the loop after modifying the first occurrence
    else:
        print("Book not found.")   


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

# View books
#def view():


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
            if not any(oldInfo):
                print("Please enter at least one old book feature.")
                break
            else:
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
