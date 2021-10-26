def display_chars(filePath, numberCharacters):
    file = open(filePath)
    partial_data = file.read(numberCharacters)
    print(f"The first {numberCharacters} characters are:\n{partial_data}\n")
    file.close()


def display_line(filePath):
    with open(filePath) as file:
        line = file.readline().strip()
        print(f"The first line is:\n{line}\n")


def display_text(filePath):
    with open(filePath) as file:
        data = file.read()
        # This would split the full text in lines
        # lines = data.split('\n')
        print(f"The full text is:\n{data}\n")


def run(filePath, numberCharacters):
    display_chars(filePath, numberCharacters)
    display_line(filePath)
    display_text(filePath)


if __name__ == "__main__":
    run("library.txt", 5)
