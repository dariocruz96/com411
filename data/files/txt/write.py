def search(filePath):
    print("Searching...", end="")
    sections = ""
    books = "Books:\n"

    with open(filePath) as file:
        for line in file:
            data = line.split(":")
            if data[0] == "Section":
                sections += line
            elif data[0] != "Section":
                books += line
    print("Done!")
    return f"{sections}\n\n{books}"


def save(filePath, storedData):
    print("Saving...", end="")
    with open(filePath, "w") as file:
        file.write(storedData)
    print("Done!")


def run():
    data = search("books.txt")
    save("sections-books.txt", data)


run()
